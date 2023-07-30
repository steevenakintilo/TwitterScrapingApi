from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import traceback

from selenium.webdriver import ActionChains
from src.user.type import *

import pyperclip

def dm_an_user(selenium_session,user,text):
    try:
        selenium_session.driver.get("https://twitter.com/"+user)
        try:
            element = WebDriverWait(selenium_session.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="sendDMFromProfile"]')))
        except:
            print("You can't dm the user")
            return(False)
        if len(text) == 0:
            text = "."
        dm_button = selenium_session.driver.find_element(By.CSS_SELECTOR,'[data-testid="sendDMFromProfile"]')
        dm_button.click()

        element = WebDriverWait(selenium_session.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="dmComposerTextInput"]')))

        text_box = selenium_session.driver.find_element(By.CSS_SELECTOR,'[data-testid="dmComposerTextInput"]')
        text_box.click()
        time.sleep(0.5)

        pyperclip.copy(text)
        act = ActionChains(selenium_session.driver)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        
        send_dm = selenium_session.driver.find_element(By.CSS_SELECTOR,'[data-testid="dmComposerSendButton"]')
        send_dm.click()
        time.sleep(0.5)

        return True
    except Exception as e:        
        if is_account_banned(selenium_session,user) == True:
            print("Account is banned DM error")
        elif is_account_existing(selenium_session,user) == True:
            print("Account is banned DM error")
        elif is_account_blocking_you(selenium_session,user) == True:
            print("Account is blocking you DM error")
        else:
            print("DM error or you don't have twitter blue")    
        return False