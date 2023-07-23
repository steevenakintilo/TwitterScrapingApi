from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import *
from src.util.list import *
import time

def follow_an_account(S,account):
    try:
        S.driver.get("https://twitter.com/"+account)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'[data-testid="placementTracking"]')))
        follow_button = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="placementTracking"]')
        if follow_button.text != "Follow":
            return (True)
        follow_button.click()
    except Exception as e:
        print("Follow account error")
        return (False)

def unfollow_an_account(S,account):
    try:
        S.driver.get("https://twitter.com/"+account)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'[data-testid="placementTracking"]')))
        unfollow_button = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="placementTracking"]')
        if unfollow_button.text != "Following":
            return (True)
        unfollow_button.click()
        click_confirm = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="confirmationSheetConfirm"]')
        click_confirm.click()
    except Exception as e:
        print("Unfollow account error")
        return (False)

def check_if_user_follow(S,account):
    try:
        S.driver.get("https://twitter.com/"+account)
        try:
            element = WebDriverWait(S.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'[data-testid="userFollowIndicator"]')))
            return True
        except:
            return False
    except Exception as e:
            return False
