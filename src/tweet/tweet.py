from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.string import *
import time

def make_a_tweet(S,text="",media=False,filepath=""):
    try:
        if len(text) == 0 or len(text) > 240:
            print("Text lenght must be between 1 and 240")
            return ("")

        S.driver.get("https://twitter.com/compose/tweet")
        time.sleep(1.5)
        #print("coment part one")
        
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')))
        
        textbox = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
        textbox.click()
        time.sleep(1.5)
        if contains_emoji(text) == True:
            text = remove_emojie(text)
        
        textbox.send_keys(text)
        
        if media == True:
            file_input = S.driver.find_element(By.XPATH,"//input[@type='file']")
            file_input.send_keys(filepath)
        
        #print("coment part two")
        time.sleep(1.5)
        
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        wait = WebDriverWait(S.driver, 10)
        target_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        S.driver.execute_script("arguments[0].scrollIntoView();", target_element)

        target_element.click()
        # try:
        #     target_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))
        #     print("Duplicate Tweet try another tweet")
        #     return("")
        # except:
        #     pass
        
        time.sleep(1.5)

        #print("comment part three")
        print("Tweet done")
        
    except Exception as e:
        if "File not found" in str(e):
            print("Can't tweet file not found")
        elif "Message: invalid argument: 'text' is empty" in str(e):
            print("Media set to true nbut no media added")
        else:
            print("tweet error")



def delete_a_tweet(S,url):
    try:
        S.driver.get(url)
        time.sleep(1.5)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="caret"]')))
        optionbox = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="caret"]')
        optionbox.click()
        time.sleep(0.1)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="Dropdown"]')))
        wait = WebDriverWait(S.driver, 10)
        target_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="Dropdown"]')))
        tweet_option = str(target_element.text).split("\n")
        if tweet_option[0] == "Delete":
            element = WebDriverWait(S.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div[1]')))
            element.click()
            element = WebDriverWait(S.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="confirmationSheetConfirm"]')))
            element.click()
            print("Tweet deleted")
            time.sleep(100)
        else:
            print("You can't delete another person tweet")
            return("")
        
    except Exception as e:
        print("Tweet delete error")