#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "10439776"))
API_HASH = environ.get("API_HASH", "ef829dab54bba2ba304fbee837315058")
BOT_TOKEN = environ.get("BOT_TOKEN", "7284233498:AAFINwQ7VviOOmQQLNrA_1slD8OJBESuAYA")
OWNER = int(environ.get("OWNER", "6182452189"))
CREDIT = environ.get("CREDIT", "Vedic")

TOTAL_USER = os.environ.get('TOTAL_USERS', '6182452189').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '-1002756256056').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
