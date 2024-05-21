class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6765826972"
    sudo_users = "6845325416", "6765826972"
    GROUP_ID = -1002133191051
    TOKEN = "6707490163:AAHZzqjm3rbEZsObRiNaT7DMtw_i5WPo_0o"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://t.me/oglogbots/4485", "https://t.me/oglogbots/4486"]
    SUPPORT_CHAT = "aboutsyanx"
    UPDATE_CHAT = "syanxx_net"
    BOT_USERNAME = "Syn_Ixbot"
    CHARA_CHANNEL_ID = "-1002115990090"
    api_id = 27704736
    api_hash = "2995e94e0f86a95fd97a156ee1d91639"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
