import os, sys
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class InstaBot:
  def __init__(self, username, password):
    chrome_option = Options()
    chrome_option.add_argument('--headless')
    
    
    self.username = username
    self.password = password
    
    self.driver = webdriver.Chrome(InstaBot._get_os())
    self.driver.get(f'https://instagram.com/{self.username}')
    # simple wait
    self.driver.implicitly_wait(20)
  
  def login(self):
    """ Will log the user in """
    
    # NOTE: need to wait for the login area to be fully loaded
    # ID for the the form is loginForm 
    # self.navigate_to_login()
    
    login_username = self.driver.find_element_by_name('username')
    login_username.click()
    login_username.send_keys(self.username)
    
    login_password = self.driver.find_element_by_name('password')
    login_password.click()
    login_password.send_keys(self.password)
    
    button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    button.click()
    
    self._remove_save_login_msg()
    self._remove_notification_msg()
    self._navigate_to_account()
    
    print("loggin in...")
    
  def _remove_save_login_msg(self):
    """ This will remove the modal that appears that asks the users 
        if they want to save their information
    """
    
    not_now_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    not_now_button.click()
    
  def _remove_notification_msg(self):
    """ This will remove the notification modal """
    
    not_now_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
    not_now_button.click()  
    
  def _navigate_to_account(self):
    """ Will navigate the bot to users account """
    self.driver.get(f'https://instagram.com/{self.username}')
      
  
  @classmethod
  def _get_os(cls):
    """ will correctly select the path for the correct os """
    
    if sys.platform == "darwin":
      return os.path.abspath('mac/chromedriver')
    elif sys.platform == "win32":
      return os.path.abspath('win/chromedriver.exe')
    