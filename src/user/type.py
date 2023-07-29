from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def is_account_private(selenium_session,account):
    try:
        selenium_session.driver.get("https://twitter.com/"+account)
        element = WebDriverWait(selenium_session.driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'[data-testid="icon-lock"]')))
        return (True)
    except Exception as e:
        return (False)

def is_account_banned(selenium_session,account):
    try:
        selenium_session.driver.get("https://twitter.com/"+account)
        element = WebDriverWait(selenium_session.driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'[data-testid="empty_state_header_text"]')))
        if "Account suspended" in element.text:
          return (True)
        return (False)
    except Exception as e:
        return (False)

def is_account_blocking_you(selenium_session,account):
    try:
        selenium_session.driver.get("https://twitter.com/"+account)
        element = WebDriverWait(selenium_session.driver,3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'[data-testid="empty_state_header_text"]')))
        if "You’re blocked" in element.text:
          return (True)
        return (False)
    except Exception as e:
        return (False)

def is_account_existing(selenium_session,account):
    try:
        selenium_session.driver.get("https://twitter.com/"+account)
        element = WebDriverWait(selenium_session.driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'[data-testid="empty_state_header_text"]')))
        if "This account doesn’t exist" in element.text:
          return (True)
        return (False)
    except Exception as e:
        return (False)