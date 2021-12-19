import os
from insta_bot import InstaBot
from dotenv import load_dotenv

load_dotenv()

username = os.environ.get('INSTA_USERNAME')
password = os.environ.get('INSTA_PASSWORD')
print(username)
bot = InstaBot(username, password)
bot.login()