from os import environ


SESSION_CONFIGS = [
    dict(
        name='scd', # Solo -> Centralized -> Decentralized
        app_sequence=['Instruction_init', 
                      'Instruction_solo', 
                      'solo', 
                      'Instruction_cen', 
                      'cen', 
                      'Instruction_dec',
                      'dec', 
                      'Instruction_end'], 
        num_demo_participants=3
    ), 
    dict(
        name='cds', # Centralized -> Decentralized -> Solo
        app_sequence=['Instruction_init', 
                      'Instruction_cen', 
                      'cen', 
                      'Instruction_dec',
                      'dec', 
                      'Instruction_solo', 
                      'solo', 
                      'Instruction_end'], 
        num_demo_participants=3
    ), 
    dict(
        name='dsc', # Decentralized -> Solo -> Centralized
        app_sequence=['Instruction_init', 
                      'Instruction_dec',
                      'dec', 
                      'Instruction_solo', 
                      'solo', 
                      'Instruction_cen', 
                      'cen', 
                      'Instruction_end'], 
        num_demo_participants=3
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=1200.00, doc=""
)

PARTICIPANT_FIELDS = ['progress', 'total_payoff']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'JPY'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'jikkenn'

DEMO_PAGE_INTRO_HTML = """
多腕バンディット課題
"""

AUTH_LEVEL = 'DEMO'

SECRET_KEY = '1881371091085'

INSTALLED_APPS = ['otree']
