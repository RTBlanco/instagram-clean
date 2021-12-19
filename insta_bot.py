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
    
    # simple wait
    self.driver.implicitly_wait(3)
  
  def login(self,username, password):
    """Will log the user in"""
    
    # NOTE: need to wait for the login area to be fully loaded
    # ID for the the form is loginForm 
    
    login_username = self.driver.find_element_by_name('username')
    login_username.click()
    login_username.send_keys(username)
    
    login_password = self.driver.find_element_by_name('password')
    login_password.click()
    login_password.send_keys(password)
    
    button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    button.click()
    
    print("loggin in...")
    
  def _remove_save_login_msg(self):
    """ This will remove the modal that appears that asks the users 
        if they want to save their information
    """
    pass
  
  @classmethod
  def _get_os(cls):
    """ will correctly select the path for the correct os """
    
    if sys.platform == "darwin":
      return os.path.abspath('mac/chromedriver')
    elif sys.platform == "win32":
      return os.path.abspath('win/chromedriver.exe')
    