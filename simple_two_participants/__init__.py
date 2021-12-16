from otree.api import *
import random
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
    name_in_url = 'solid_javascript'
    players_per_group = 2
    num_rounds = 30

    with open('phaser/reward.csv', encoding='utf-8') as file:
        rows = list(csv.reader(file))


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


"""
##############################
 Pages
##############################
"""
class Task(Page):
    @staticmethod
    def js_vars(player):
        partner = get_partner(player)
        if player.round_number == 1:
            my_partner_previous = None
            my_previous_choice = None
            my_previous_reward = None
        else:
            my_partner_previous_raw = partner.in_round(player.round_number - 1).choice
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
            rewards = Constants.rows,
            my_partner_previous = my_partner_previous,
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
    form_fields = ['choice', 'reward']


class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    pass


"""
##############################
 Functions
##############################
"""
def get_partner(player):
    return player.get_others_in_group()[0]


"""
##############################
 Page sequence
##############################
"""
page_sequence = [Task, ResultsWaitPage]
