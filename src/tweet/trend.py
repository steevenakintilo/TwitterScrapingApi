from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


from src.util.string import *
import time

import traceback


def get_trend(S):
    try:
      S.driver.get("https://twitter.com/explore")
      element = WebDriverWait(S.driver, 15).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="trend"]')))
      trends = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="trend"]')
      trends_list = []
      pos = 0
      for i in range(len(trends)):
          r = trends[i]
          trends_list.append(r.text.split("\n")[1])
      return(trends_list)
    except Exception as e:
        print("Trend error")
        return ([])