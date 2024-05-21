class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6385717717"
    sudo_users = "7119919871", "6449855012"
    GROUP_ID = -1002117519350
    TOKEN = "6800291183:AAGs5EoxtJjLxxWziF4W-VWG83bld9ryhgk"
    mongo_url = "mongodb+srv://Arman121:Arman121@arman.ji8gqxd.mongodb.net/?retryWrites=true&w=majority"
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
