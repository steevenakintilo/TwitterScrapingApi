from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.tweet.info import is_tweet_exist

import time

def like_a_tweet(selenium_session,url):
    try:
        selenium_session.driver.get(url)
        pos = 0
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')))
        
        tweet_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
        for i in range(len(tweet_info)):
            r = tweet_info[i]
            if url.split("twitter.com")[1] in str(r.get_attribute("outerHTML")):
                pos = i
                break
        
        tweets_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')

        for i in range(len(tweet_info)):
            lower_data = str(tweet_info[i].get_property('outerHTML')).lower()
            if i == pos:
                if "unlike" in lower_data:
                    print("Tweet is already liked")
                    return True
        
        
        element = WebDriverWait(selenium_session.driver,15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="like"]')))
    
        like_button = selenium_session.driver.find_elements(By.CSS_SELECTOR,'[data-testid="like"]')
        time.sleep(0.5)
        if pos > len(like_button):
            print("ok")
            like_button[len(like_button) - 1].click()
        else:
            try:
                print("be")
                like_button[pos].click()
            except:
                print("sum")
                like_button[pos-1].click()
        
    except Exception as e:
        if is_tweet_exist(selenium_session,url) == False:
            print("Tweet don't exist , like error")
        else:
            print("Like error")
        return False


def unlike_a_tweet(selenium_session,url):
    try:
        selenium_session.driver.get(url)
        pos = 0
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')))
        
        tweet_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
        for i in range(len(tweet_info)):
            r = tweet_info[i]
            if url.split("twitter.com")[1] in str(r.get_attribute("outerHTML")):
                pos = i
                break
        
        tweets_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')

        for i in range(len(tweet_info)):
            lower_data = str(tweet_info[i].get_property('outerHTML')).lower()
            if i == pos:
                if "unlike" not in lower_data:
                    print("Tweet is already unliked")
                    return True
        
        
        element = WebDriverWait(selenium_session.driver,15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="unlike"]')))
    
        like_button = selenium_session.driver.find_elements(By.CSS_SELECTOR,'[data-testid="unlike"]')
        time.sleep(0.5)
        if pos > len(like_button):
            like_button[len(like_button) - 1].click()
        else:
            try:
                like_button[pos].click()
            except:
                like_button[pos-1].click()

    except Exception as e:
        if is_tweet_exist(selenium_session,url) == False:
            print("Tweet don't exist , unlike error")
        else:
            print("Unike error")
        return False

    
def check_if_tweet_liked(selenium_session,url):
    try:
        selenium_session.driver.get(url)
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="like"]')))
        
        like_button = selenium_session.driver.find_element(By.CSS_SELECTOR,'[data-testid="like"]')
        
        liked_or_not = like_button.get_attribute("aria-label")

        if liked_or_not.lower() == "like":
            return False
        else:
            return True
    except Exception as e:
        print("Like error")
        return False
        