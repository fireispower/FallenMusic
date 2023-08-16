from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("7350195"))
API_HASH = getenv("b4105c3fddc4474048dfe79683555d0c")

BOT_TOKEN = getenv("6412599320:AAFde10xeuFFaSfGOnbDVL57jATTtBQDMF8", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("817237333"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/enigma_mainchat")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/enigmaunion")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "724516516").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
