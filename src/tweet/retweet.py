from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.tweet.info import is_tweet_exist

from src.util.string import *
import time

from selenium.webdriver import ActionChains

import pyperclip

def retweet_a_tweet(S,url):

    try:
        S.driver.get(url)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')))
        tweet_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
        pos = 0
        for i in range(len(tweet_info)):
            r = tweet_info[i]
            if url.split("twitter.com")[1] in str(r.get_attribute("outerHTML")):
                pos = i
                break
        
        element = WebDriverWait(S.driver,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="retweet"]'))
        )
    
        retweet_button = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="retweet"]')
        retweet_button[pos].click()

        element = WebDriverWait(S.driver,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="retweetConfirm"]'))
        )
                   
        retweet_button = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="retweetConfirm"]')
        retweet_button.click()
        time.sleep(0.5)
        return True
    
    except Exception as e:
        if is_tweet_exist(S,url) == False:
            print("Tweet don't exist , retweet error")
        else:
            print("Tweet is already retweet, retweet error")
        return False        

def unretweet_a_tweet(S,url):

    try:
        S.driver.get(url)
        element = WebDriverWait(S.driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')))
        tweet_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
        pos = 0
        for i in range(len(tweet_info)):
            r = tweet_info[i]
            if url.split("twitter.com")[1] in str(r.get_attribute("outerHTML")):
                pos = i
                break

        element = WebDriverWait(S.driver,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="unretweet"]'))
        )

        unretweet_button = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="unretweet"]')
        unretweet_button[pos].click()
        
        element = WebDriverWait(S.driver,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="unretweetConfirm"]'))
        )
        
        unretweet_button = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="unretweetConfirm"]')
        unretweet_button.click()
        
        return True

    except Exception as e:
        if is_tweet_exist(S,url) == False:
            print("Tweet don't exist , unretweet error")
        else:
            print("Tweet is already retweet, retweet error")
        return False
    
        
def check_if_tweet_retweet(S,url):
    try:
        S.driver.get(url)
        try:
            element = WebDriverWait(S.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="retweet"]')))
            return False
        except:
            pass
        try:        
            element = WebDriverWait(S.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="unretweet"]')))
            return True
        except:
            pass    
        return False

    except Exception as e:
        if is_tweet_exist(S,url) == False:
            print("Tweet don't exist , can't check if the tweet is retweet")
        else:
            print("Checking retweet error")
        
def quote_a_tweet(S,url,text="",media=False,filepath=""):
    
    try:
        if len(text) == 0:
            text = "."
        if len(text) == 0 or len(text) > 280:
            text = text[0:279]
        S.driver.get(url)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="retweet"]')))
        
        retweet_button = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="retweet"]')
        retweet_button.click()

        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[href="/compose/tweet"]')))
        
        quote_button = S.driver.find_element(By.CSS_SELECTOR, '[href="/compose/tweet"]')
        quote_button.click()
        
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')))
        
        textbox = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
        textbox.click()
        
        pyperclip.copy(text)
        act = ActionChains(S.driver)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

        
        if media == True:
            file_input = S.driver.find_element(By.XPATH,"//input[@type='file']")
            file_input.send_keys(filepath)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        wait = WebDriverWait(S.driver, 10)
        target_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        S.driver.execute_script("arguments[0].scrollIntoView();", target_element)

        target_element.click()
        time.sleep(1.5)
        return True
        
    except Exception as e:
        if "File not found" in str(e):
            print("Can't quote tweet file not found")
        elif "Message: invalid argument: 'text' is empty" in str(e):
            print("Media set to true nbut no media added")
        elif is_tweet_exist(S,url) == False:
            print("Tweet don't exist , quote error")   
        else:
            print("quote error")
        return False