"""
from os import getenv


API_ID = int(getenv("API_ID", "20346550"))
API_HASH = getenv("API_HASH", "bc79c3bea7a626887bdc0871eecf0327)
BOT_TOKEN = getenv("BOT_TOKEN", "7447109300:AAG2RVJClcMUIcFPagYMO3z5e3OTqTOyhJw")
OWNER_ID = int(getenv("OWNER_ID", "6622333718"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8012873547 7491167754").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002278731669"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002278731669"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

