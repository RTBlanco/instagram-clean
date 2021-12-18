import os, sys
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class InstaBot:
  def __init__(self):
    chrome_option = Options()
    chrome_option.add_argument('--headless')
    
    self.driver = webdriver.Chrome(InstaBot._get_os())
    self.driver.get('https://instagram.com/')
  
  def login():
    pass
  
  @classmethod
  def _get_os(cls):
    """ will correctly select the path for the correct os """
    
    if sys.platform == "darwin":
      return os.path.abspath('mac/chromedriver')
    elif sys.platform == "win32":
      return os.path.abspath('win/chromedriver.exe')
    