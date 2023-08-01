from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.tweet.info import is_tweet_exist

from src.util.string import *
import time

from selenium.webdriver import ActionChains
from src.util.string import get_absolute_picture_path

import pyperclip
import traceback

def retweet_a_tweet(selenium_session,url):
    try:
        selenium_session.driver.get(url)
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')))
        tweet_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
        pos = 0
        for i in range(len(tweet_info)):
            r = tweet_info[i]
            if url.split("twitter.com")[1] in str(r.get_attribute("outerHTML")):
                pos = i
                break
        
        tweets_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')

        for i in range(len(tweet_info)):
            lower_data = str(tweet_info[i].get_property('outerHTML')).lower()
            if i == pos:
                if "unretweet" in lower_data:
                    return True
                
        element = WebDriverWait(selenium_session.driver,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="retweet"]'))
        )
    
        retweet_button = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="retweet"]')
        if pos > len(retweet_button):
            retweet_button[len(retweet_button) - 1].click()
        else:
            try:
                retweet_button[pos].click()
            except:
                retweet_button[pos-1].click()
        element = WebDriverWait(selenium_session.driver,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="retweetConfirm"]'))
        )
                   
        retweet_button = selenium_session.driver.find_element(By.CSS_SELECTOR, '[data-testid="retweetConfirm"]')
        retweet_button.click()
        time.sleep(1)
        return True
    
    except Exception as e:
        if is_tweet_exist(selenium_session,url) == False:
            print("Tweet don't exist , retweet error")
        else:
            return True
        return False        

def unretweet_a_tweet(selenium_session,url):
    try:
        selenium_session.driver.get(url)
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')))
        tweet_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
        pos = 0
        for i in range(len(tweet_info)):
            r = tweet_info[i]
            if url.split("twitter.com")[1] in str(r.get_attribute("outerHTML")):
                pos = i
                break
        
        tweets_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')

        for i in range(len(tweet_info)):
            lower_data = str(tweet_info[i].get_property('outerHTML')).lower()
            if i == pos:
                if "unretweet" not in lower_data:
                    return True
                
        element = WebDriverWait(selenium_session.driver,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="unretweet"]'))
        )
    
        retweet_button = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="unretweet"]')
        if pos > len(retweet_button):
            retweet_button[len(retweet_button) - 1].click()
        else:
            try:
                retweet_button[pos].click()
            except:
                retweet_button[pos-1].click()

        element = WebDriverWait(selenium_session.driver,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="unretweetConfirm"]'))
        )
                   
        retweet_button = selenium_session.driver.find_element(By.CSS_SELECTOR, '[data-testid="unretweetConfirm"]')
        retweet_button.click()
        time.sleep(1)
        return True
    
    except Exception as e:
        if is_tweet_exist(selenium_session,url) == False:
            print("Tweet don't exist , retweet error")
        else:
            return True
        return False        

def check_if_tweet_retweet(selenium_session,url):
    try:
        selenium_session.driver.get(url)
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')))
        tweet_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
        pos = 0
        for i in range(len(tweet_info)):
            r = tweet_info[i]
            if url.split("twitter.com")[1] in str(r.get_attribute("outerHTML")):
                pos = i
                break
        
        tweets_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')

        for i in range(len(tweet_info)):
            lower_data = str(tweet_info[i].get_property('outerHTML')).lower()
            if i == pos:
                if "unretweet" in lower_data:
                    return True
                
        return False
    except Exception as e:
        if is_tweet_exist(selenium_session,url) == False:
            print("Tweet don't exist , retweet error")
        else:
            return True
        return False        

        
def quote_a_tweet(selenium_session,url,text=""):
    
    try:
        rt = False
        if len(text) == 0:
            text = "."
        if len(text) == 0 or len(text) > 280:
            text = text[0:279]
        selenium_session.driver.get(url)
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')))
        tweet_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
        pos = 0
        for i in range(len(tweet_info)):
            r = tweet_info[i]
            if url.split("twitter.com")[1] in str(r.get_attribute("outerHTML")):
                pos = i
                break
        
        tweets_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
        
        element = WebDriverWait(selenium_session.driver,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="retweet"]'))
        )

        for i in range(len(tweet_info)):
            lower_data = str(tweet_info[i].get_property('outerHTML')).lower()
            if i == pos:
                if "unretweet" not in lower_data:
                    rt = False
        
        if rt == False:
            element = WebDriverWait(selenium_session.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="retweet"]')))
        
            retweet_button = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="retweet"]')
        else:
            element = WebDriverWait(selenium_session.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="unretweet"]')))
        
            retweet_button = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="unretweet"]')
            
        if pos > len(retweet_button):
            retweet_button[len(retweet_button) - 1].click()
        else:
            try:
                retweet_button[pos].click()
            except:
                retweet_button[pos-1].click()
            
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[href="/compose/tweet"]')))
        
        quote_button = selenium_session.driver.find_element(By.CSS_SELECTOR, '[href="/compose/tweet"]')
        quote_button.click()
        
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')))
        
        pyperclip.copy(text)
        act = ActionChains(selenium_session.driver)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        wait = WebDriverWait(selenium_session.driver, 10)
        target_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        selenium_session.driver.execute_script("arguments[0].scrollIntoView();", target_element)
        
        time.sleep(1.5)
        target_element.click()
        time.sleep(1.5)
        return True
        
    except Exception as e:
        if is_tweet_exist(selenium_session,url) == False:
            print("Tweet don't exist , quote error")   
        else:
            print("quote error")
        return False

def quote_a_tweet_with_media(selenium_session,url,text="",filepath="",type="pic"):
    try:
        rt = False
        filepath = get_absolute_picture_path(filepath)
        if len(text) == 0:
            text = "."
        if len(text) == 0 or len(text) > 280:
            text = text[0:279]
        selenium_session.driver.get(url)

        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')))
        tweet_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
        pos = 0
        for i in range(len(tweet_info)):
            r = tweet_info[i]
            if url.split("twitter.com")[1] in str(r.get_attribute("outerHTML")):
                pos = i
                break
        
        tweets_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
        
        element = WebDriverWait(selenium_session.driver,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="retweet"]'))
        )

        for i in range(len(tweet_info)):
            lower_data = str(tweet_info[i].get_property('outerHTML')).lower()
            if i == pos:
                if "unretweet" not in lower_data:
                    rt = False
        
        if rt == False:
            element = WebDriverWait(selenium_session.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="retweet"]')))
        
            retweet_button = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="retweet"]')
        else:
            element = WebDriverWait(selenium_session.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="unretweet"]')))
        
            retweet_button = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="unretweet"]')
        
            
        if pos > len(retweet_button):
            retweet_button[len(retweet_button) - 1].click()
        else:
            try:
                retweet_button[pos].click()
            except:
                retweet_button[pos-1].click()
            
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[href="/compose/tweet"]')))
        
        quote_button = selenium_session.driver.find_element(By.CSS_SELECTOR, '[href="/compose/tweet"]')
        quote_button.click()
        
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')))
        
        pyperclip.copy(text)
        act = ActionChains(selenium_session.driver)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        
        file_input = selenium_session.driver.find_element(By.XPATH,"//input[@type='file']")
        file_input.send_keys(filepath)
        
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        wait = WebDriverWait(selenium_session.driver, 10)
        target_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        selenium_session.driver.execute_script("arguments[0].scrollIntoView();", target_element)
        if type == "video":
            time.sleep(60)
        
        time.sleep(1.5)
        target_element.click()
        if type == "video":
            time.sleep(30)
        time.sleep(1.5)
        return True        
    except Exception as e:
        if "File not found" in str(e):
            print("Can't quote tweet file not found")
        elif "Message: invalid argument: 'text' is empty" in str(e):
            print("Media set to true nbut no media added")
        elif is_tweet_exist(selenium_session,url) == False:
            print("Tweet don't exist , quote error")   
        else:
            print("quote with media error")
        return False