import dotenv
import os
import json
from dotenv import load_dotenv
load_dotenv()

##LANG START
import locales
from locales import es
from locales import en
#Need Help Importing Language Stuff
##LANG END

TOKEN = os.environ.get("TOKEN")
DEFAULT_PREFIX = os.environ.get("TOKEN")
BOT_OWNER = os.environ.get("TOKEN")
BOT_DEVELOPER = os.environ.get("TOKEN")
DB_URI = os.environ.get("TOKEN")