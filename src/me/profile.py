from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import *
from src.util.list import *

import time
import traceback

def change_bio(S,text):
    if len(text) > 160:
        text = text[0:159]
    try:
        S.driver.get("https://twitter.com/settings/profile")
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.NAME, 'description')))
        bio_box = S.driver.find_element(By.NAME, 'description')
        time.sleep(0.5)
        bio_box.clear()
        bio_box.send_keys(text)
        time.sleep(0.5)
        save_input = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="Profile_Save_Button"]')
        save_input.click()

    except Exception as e:
        print("Bio error")



def change_name(S,text):
    if len(text) > 50:
        text = text[0:49]
    try:
        S.driver.get("https://twitter.com/settings/profile")
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.NAME, 'displayName')))
        name_box = S.driver.find_element(By.NAME, 'displayName')
        time.sleep(0.5)
        name_box.clear()
        name_box.send_keys(text)
        time.sleep(0.5)
        save_input = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="Profile_Save_Button"]')
        save_input.click()
        
    except Exception as e:
        print("Name error")



def change_location(S,text):
    if len(text) > 30:
        text = text[0:29]
    try:
        S.driver.get("https://twitter.com/settings/profile")
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.NAME, 'location')))
        location_box = S.driver.find_element(By.NAME, 'location')
        time.sleep(0.5)
        location_box.clear()
        location_box.send_keys(text)
        time.sleep(0.5)
        save_input = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="Profile_Save_Button"]')
        save_input.click()
        
    except Exception as e:
        print("Location error")


def change_url(S,text):
    if len(text) > 100:
        text = text[0:99]
    try:
        S.driver.get("https://twitter.com/settings/profile")
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.NAME, 'url')))
        url_box = S.driver.find_element(By.NAME, 'url')
        time.sleep(0.5)
        url_box.clear()
        url_box.send_keys(text)
        time.sleep(0.5)
        save_input = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="Profile_Save_Button"]')
        save_input.click()
        
    except Exception as e:
        print("Url error")


def change_profile_picture(S,filepath):
    try:
        S.driver.get("https://twitter.com/settings/profile")
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'[data-testid="fileInput"]')))
        name_box = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="fileInput"]')
        S.driver.execute_script("arguments[0].scrollIntoView();", name_box)
        #name_box.click()
        time.sleep(50000)
        #name_box.send_keys(filepath)
    
        #time.sleep(0.5)
        #save_input = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="Profile_Save_Button"]')
        #save_input.click()
        
    except Exception as e:
        if "File not found" in str(e):
            print("Can't change profile picture file not found")
        else:
            print("Profile picture error")
            print(e)