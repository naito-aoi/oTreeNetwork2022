from otree.api import *

doc = """
最初のインストラクション
"""

"""
##############################
 Models
##############################
"""
class Constants(BaseConstants):
    name_in_url = 'init_instruction'
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
class InformedConsent(Page):
    pass

class Instruction1(Page):
    pass

class Instruction2(Page):
    pass


"""
##############################
 Page sequence
##############################
"""
page_sequence = [InformedConsent, Instruction1, Instruction2]
