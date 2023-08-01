from src.start import *
from src.scrapper import *

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def check_language(selenium_session):
      url = "https://twitter.com/MrBeast/status/1523674759925760000"
      selenium_session.driver.get(url)
      element = WebDriverWait(selenium_session.driver, 15).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
      tweet_info = selenium_session.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweet"]')
      lower_data = str(tweet_info.get_property('outerHTML')).lower()
      if "share tweet" not in lower_data:
          return False
      return True

selenium_session = start_selenium()
language = check_language(selenium_session)
if language == True:
     print("You can use the code")
else:
     print("You can't use the code right now but don't worries an update will fix this problem soon")