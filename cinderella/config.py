# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os

def get_user_list(config, key):
    with open('{}/cinderella/{}'.format(os.getcwd(), config), 'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1759961454:AAEaSSkSus0W4aI6q1N3FnDwNlnWKyC0kLc"
    OWNER_ID = "606837450"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "info_eater"
    TELETHON_HASH = "378d1e1d6437ef6fc1c15fd031b6ac3b"  # for purge stuffs
    TELETHON_ID = "3091593"
    
    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://jclzmlbfalxqxt:9f0a7d1abba0d93fc40d0f6dea75f158358f85f4c5319e4a895ce8e3cfa595f4@ec2-54-211-176-156.compute-1.amazonaws.com:5432/d56qk6flhc2liu'  # needed for any database modules
    MESSAGE_DUMP = "-511683396"  # needed to make sure 'save from' messages persist
    GBAN_LOGS = "-1001200945135"
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None

    # OPTIONAL
    #ID Seperation format [1,2,3,4]
    SUDO_USERS = get_user_list('elevated_users.json', 'sudos')  # List of id's -  (not usernames) for users which have sudo access to the bot.
    DEV_USERS = get_user_list('elevated_users.json', 'devs')  # List of id's - (not usernames) for developers who will have the same perms as the owner
    SUPPORT_USERS = get_user_list('elevated_users.json', 'supports')  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = get_user_list('elevated_users.json', 'whitelists')  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    SPAMMERS = None
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    STRICT_GMUTE = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAACAgUAAxkBAAIHsl5nbqXdDTmpG2HFDNhnwvE5kFbWAAI9AQAC3pTNLzeTCUmnhTneGAQ'  # banhammer marie sticker
    ALLOW_EXCL = True  # Allow ! commands as well as /
    CASH_API_KEY = "K2U4TK3KSLID8XU9" # Get one from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = "B4A8RSSVUGHR" # Get one from https://timezonedb.com/register
    WALL_API = None
    LASTFM_API_KEY = "4e365ba060ff46da6a20f0342ec203b2"
    LYDIA_API = "5e1b5faf8265d161da66d481f7677161914b0cb3497bb1e7280a5cc50945cc3ba3f934889059673021636ea0578d0158cb14a1bf5d99359062e2942b19e5a611"
    API_OPENWEATHER = "1850cf75ad426f3e0ccaaecc900ad183"
    
   
  
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
