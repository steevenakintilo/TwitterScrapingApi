from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.string import *
import time

def reetweet_a_tweet(S,url):

    try:
        S.driver.get(url)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="retweet"]')))
        
        reetweet_button = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="retweet"]')
        reetweet_button.click()

        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="retweetConfirm"]')))
        
        reetweet_button = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="retweetConfirm"]')
        reetweet_button.click()
        
        print("reetweet done")
    except Exception as e: 
        print("retweet error")
        

def unreetweet_a_tweet(S,url):

    try:
        S.driver.get(url)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="unretweet"]')))
        
        unreetweet_button = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="unretweet"]')
        unreetweet_button.click()

        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="unretweetConfirm"]')))
        
        unreetweet_button = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="unretweetConfirm"]')
        unreetweet_button.click()
        
        print("reetweet done")
    except Exception as e: 
        print("retweet error")
        

def quote_a_tweet(S,url,text="",media=False,filepath=""):
    
    try:
        if len(text) == 0 or len(text) > 240:
            print("Text lenght must be between 1 and 240")
            pass
        S.driver.get(url)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="retweet"]')))
        
        reetweet_button = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="retweet"]')
        reetweet_button.click()

        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[href="/compose/tweet"]')))
        
        quote_button = S.driver.find_element(By.CSS_SELECTOR, '[href="/compose/tweet"]')
        quote_button.click()
        
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')))
        
        textbox = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
        textbox.click()
        if contains_emoji(text) == True:
            text = remove_emojie(text)
        
        textbox.send_keys(text)
        
        
        if media == True:
            file_input = S.driver.find_element(By.XPATH,"//input[@type='file']")
            file_input.send_keys(filepath)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        wait = WebDriverWait(S.driver, 10)
        target_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        S.driver.execute_script("arguments[0].scrollIntoView();", target_element)

        target_element.click()
        # time.sleep(0.5)
        # try:
        #     target_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))
        #     print("Duplicate Tweet try another tweet")
        #     return("")
        # except:
        #     pass
        time.sleep(2)
        
    except Exception as e:
        if "File not found" in str(e):
            print("Can't quote tweet file not found")
        elif "Message: invalid argument: 'text' is empty" in str(e):
            print("Media set to true nbut no media added")
        else:
            print("quote error")        