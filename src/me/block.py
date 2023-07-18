from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import traceback

def block_an_user(S,user):
    try:
        S.driver.get("https://twitter.com/"+user)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="userActions"]')))

        user_option = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="userActions"]')
        user_option.click()

        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="block"]')))

        block_btn = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="block"]')
        S.driver.execute_script("arguments[0].scrollIntoView();", block_btn)
        block_btn.click()

        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="confirmationSheetConfirm"]')))

        confirm_block = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="confirmationSheetConfirm"]')
        confirm_block.click()

        time.sleep(0.1)
    except Exception as e:
        print("Blocking error")

def unblock_an_user(S,user):
    try:
        S.driver.get("https://twitter.com/"+user)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="userActions"]')))

        user_option = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="userActions"]')
        user_option.click()

        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="block"]')))

        unblock_btn = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="block"]')
        S.driver.execute_script("arguments[0].scrollIntoView();", unblock_btn)
        unblock_btn.click()

        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="confirmationSheetConfirm"]')))

        confirm_unblock = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="confirmationSheetConfirm"]')
        confirm_unblock.click()

        time.sleep(0.1)
    
    except Exception as e:
        print("Unblocking error")
