from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import *
from src.util.list import *

import time
import traceback

def change_bio(selenium_session,text):
    if len(text) > 160:
        text = text[0:159]
    if len(text) == 0:
        text = "."
    try:
        selenium_session.driver.get("https://twitter.com/settings/profile")
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.NAME, 'description')))
        bio_box = selenium_session.driver.find_element(By.NAME, 'description')
        time.sleep(0.5)
        bio_box.clear()
        bio_box.send_keys(text)
        time.sleep(0.5)
        save_input = selenium_session.driver.find_element(By.CSS_SELECTOR,'[data-testid="Profile_Save_Button"]')
        save_input.click()
        time.sleep(1.5)
        return True
    except Exception as e:
        print("Error while changing bio")
        
        return False



def change_name(selenium_session,text):
    if len(text) > 50:
        text = text[0:49]
    if len(text) == 0:
        text = "."
    try:
        selenium_session.driver.get("https://twitter.com/settings/profile")
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.NAME, 'displayName')))
        name_box = selenium_session.driver.find_element(By.NAME, 'displayName')
        time.sleep(0.5)
        name_box.clear()
        name_box.send_keys(text)
        time.sleep(0.5)
        save_input = selenium_session.driver.find_element(By.CSS_SELECTOR,'[data-testid="Profile_Save_Button"]')
        save_input.click()
        time.sleep(1.5)
        return True
        
    except Exception as e:
        print("Error while changing name")
        
        return False



def change_location(selenium_session,text):
    if len(text) > 30:
        text = text[0:29]
    if len(text) == 0:
        text = "."
    try:
        selenium_session.driver.get("https://twitter.com/settings/profile")
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.NAME, 'location')))
        location_box = selenium_session.driver.find_element(By.NAME, 'location')
        time.sleep(0.5)
        location_box.clear()
        location_box.send_keys(text)
        time.sleep(0.5)
        save_input = selenium_session.driver.find_element(By.CSS_SELECTOR,'[data-testid="Profile_Save_Button"]')
        save_input.click()
        time.sleep(1.5)
        return True
    except Exception as e:
        print("Error while changing location")
        
        return False


def change_url(selenium_session,text):
    if len(text) > 100:
        text = text[0:99]
    if len(text) == 0:
        text = "."
    
    try:
        selenium_session.driver.get("https://twitter.com/settings/profile")
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.NAME, 'url')))
        url_box = selenium_session.driver.find_element(By.NAME, 'url')
        time.sleep(0.5)
        url_box.clear()
        url_box.send_keys(text)
        time.sleep(0.5)
        save_input = selenium_session.driver.find_element(By.CSS_SELECTOR,'[data-testid="Profile_Save_Button"]')
        save_input.click()
        time.sleep(1.5)
        return True
    except Exception as e:
        print("Error while changing url")
        
        return False


def change_profile_picture(selenium_session,filepath):
    try:
        selenium_session.driver.get("https://twitter.com/settings/profile")
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'[data-testid="fileInput"]')))
        name_box = selenium_session.driver.find_element(By.CSS_SELECTOR,'[data-testid="fileInput"]')
        selenium_session.driver.execute_script("arguments[0].scrollIntoView();", name_box)
        file_input = selenium_session.driver.find_elements(By.XPATH,"//input[@type='file']")
        file_input[1].send_keys(filepath)
        apply_btn = selenium_session.driver.find_element(By.CSS_SELECTOR,'[data-testid="applyButton"]')
        apply_btn.click()
        save_input = selenium_session.driver.find_element(By.CSS_SELECTOR,'[data-testid="Profile_Save_Button"]')
        save_input.click()
        time.sleep(2)
        
        return True
        
    except Exception as e:
        if "File not found" in str(e):
            print("Can't change profile picture file not found")
        elif "unknown error: path is not absolute:" in str(e):
            print("You need to put full path of the picture")
        else:
            print("Error while changing profile picture")
        return False


def change_banner(selenium_session,filepath):
    try:
        selenium_session.driver.get("https://twitter.com/settings/profile")
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'[data-testid="fileInput"]')))
        name_box = selenium_session.driver.find_element(By.CSS_SELECTOR,'[data-testid="fileInput"]')
        selenium_session.driver.execute_script("arguments[0].scrollIntoView();", name_box)
        file_input = selenium_session.driver.find_elements(By.XPATH,"//input[@type='file']")
        file_input[0].send_keys(filepath)
        apply_btn = selenium_session.driver.find_element(By.CSS_SELECTOR,'[data-testid="applyButton"]')
        apply_btn.click()
        save_input = selenium_session.driver.find_element(By.CSS_SELECTOR,'[data-testid="Profile_Save_Button"]')
        save_input.click()
        time.sleep(2)
        
        return True
        
    except Exception as e:
        if "File not found" in str(e):
            print("Can't change banner file not found")
        elif "unknown error: path is not absolute:" in str(e):
            print("You need to put full path of the picture")
        else:
            print("Error while changing banner")
        
        return False