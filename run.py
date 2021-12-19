import os
from insta_bot import InstaBot
from dotenv import load_dotenv

load_dotenv()

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

bot = InstaBot(username, password)
bot.login()