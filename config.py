import os

API_ID = API_ID = 26112881

API_HASH = os.environ.get("API_HASH", "8898fa823ffa1810ca10cc5c77417e85")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7141314149:AAHpMh32zbOrcRZYyEPLiw-h7zP_Rbf8J-A")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1252140937))

LOG = -1001907859284,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5008977329").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


