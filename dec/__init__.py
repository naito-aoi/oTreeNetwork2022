from otree.api import *
import random
import numpy as np
import csv


doc = """
Your app description
"""

"""
##############################
 Models
##############################
"""
class Constants(BaseConstants):
    name_in_url = 'dec'
    players_per_group = 3 # グループサイズ
    num_rounds = 5 # 試行数
    num_arms = 2 # アーム数
    rows = [150, 160] # アームの期待報酬
    """
    # 報酬ファイルを取り込む場合
    with open('reward.csv', encoding='utf-8') as file:
        rows = list(csv.reader(file))
    """


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    for player in subsession.get_players():
        participant = player.participant
        participant.total_payoff = 0
        participant.progress = 1


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.IntegerField()
    reward = models.IntegerField()
    soc_0 = models.IntegerField()
    soc_1 = models.IntegerField()
    #soc_info = models.IntegerField()


"""
##############################
 Pages
##############################
"""
class Task(Page):
    @staticmethod
    def js_vars(player):
        partner_list = get_partner(player)
        partner_choice_list = [0] * Constants.num_arms
        if player.round_number == 1:
            my_partner_previous = None
            my_previous_choice = None
            my_previous_reward = None
        else:
            for partner in partner_list:
                my_partner_previous_raw = partner.in_round(player.round_number - 1).choice
                if my_partner_previous_raw != -1: # 欠損値が-1で出力されるが、pythonではリストの最後尾を参照してしまうため
                    partner_choice_list[my_partner_previous_raw] += 1
            
            my_partner_previous = my_partner_previous_raw if my_partner_previous_raw != -1 else None
            my_previous_choice = []
            my_previous_reward = []
            for i in range(1, player.round_number):
                my_previous_choice_tmp = player.in_round(i).choice
                my_previous_reward_tmp = player.in_round(i).reward
                if my_previous_choice_tmp != -1:
                    my_previous_choice.append(my_previous_choice_tmp)
                    my_previous_reward.append(my_previous_reward_tmp)

        return dict(
            past = Constants.num_rounds,
            currentRound = player.round_number,
            arrange_arms = divisor_list(Constants.num_arms),
            rewards = Constants.rows,
            my_partner_previous = my_partner_previous,
            partner_choice_list = partner_choice_list,
            my_previous_choice = my_previous_choice,
            my_previous_reward = my_previous_reward,
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        participant.total_payoff += player.in_round(player.round_number).reward
        participant.progress += 1

        if timeout_happened:
            # タイムアウト: -1 を返す
            player.choice = -1

    timeout_seconds = 12
    timer_text = '残り時間：'

    form_model = 'player'
    #form_fields = ['choice', 'reward', 'soc_info']
    form_fields = ['choice', 'reward', 'soc_0', 'soc_1']


class ResultsWaitPage(WaitPage):
    title_text = "そのままお待ちください..."
    body_text = "他の参加者が選択中です"


"""
##############################
 Functions
##############################
"""
def divisor_list(num): # アームの配置を正方形に近づけたい（i.e., 約数の計算）
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append([i, int(num/i)])  
    return sorted(divisors)[-1]


def get_partner(player):
    # ネットワーク構造

    network_structure = [
        [player.group.get_player_by_id(2)],     # id=0の隣人
        [player.group.get_player_by_id(3)],     # id=1の隣人
        [player.group.get_player_by_id(1)]      # id=2の隣人
    ]
    partner_id = network_structure[player.id_in_group-1]   

    #partners = player.get_others_in_group()
    
    #print(partners)
    #return partners
    return partner_id



"""
##############################
 Page sequence
##############################
"""
page_sequence = [Task, ResultsWaitPage]
