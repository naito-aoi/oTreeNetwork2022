from otree.api import *

doc = """
cen条件のインストラクション
"""

"""
##############################
 Models
##############################
"""
class Constants(BaseConstants):
    name_in_url = 'cen_instruction'
    players_per_group = 3 # グループサイズ
    num_rounds = 1
    num_arms = 2 # アーム数
    rows = [150, 160] # アームの期待報酬


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


"""
##############################
 Pages
##############################
"""
class Instruction1(Page):
    @staticmethod
    def js_vars(player):
        return dict(
            arrange_arms = divisor_list(Constants.num_arms),
        )

class Instruction2(Page):
    pass

class ResultsWaitPage(WaitPage):
    title_text = "そのままお待ちください..."
    body_text = "他の参加者を待っています"


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


"""
##############################
 Page sequence
##############################
"""
page_sequence = [Instruction1, Instruction2, ResultsWaitPage]
