from otree.api import *

doc = """
最後のインストラクション
"""

"""
##############################
 Models
##############################
"""
class Constants(BaseConstants):
    name_in_url = 'end_instruction'
    players_per_group = None # グループサイズ
    num_rounds = 1


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
    pass


"""
##############################
 Page sequence
##############################
"""
page_sequence = [Instruction1]
