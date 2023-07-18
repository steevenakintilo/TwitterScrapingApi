from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import traceback

from selenium.webdriver import ActionChains

import pyperclip

def dm_user(S,user,text):
    try:
        S.driver.get("https://twitter.com/"+user)
        try:
            element = WebDriverWait(S.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="sendDMFromProfile"]')))
        except:
            print("You can't dm the user")
            return("")
        dm_button = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="sendDMFromProfile"]')
        dm_button.click()

        element = WebDriverWait(S.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="dmComposerTextInput"]')))

        text_box = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="dmComposerTextInput"]')
        text_box.click()
        time.sleep(0.5)

        pyperclip.copy(text)
        act = ActionChains(S.driver)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

        send_dm = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="dmComposerSendButton"]')
        send_dm.click()
        time.sleep(0.5)
    except Exception as e:
        print("DM error or you don't have twitter blue")