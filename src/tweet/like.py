from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.tweet.info import is_tweet_exist

import time

def like_a_tweet(S,url):
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
        
        element = WebDriverWait(S.driver,15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="like"]'))
        )

        like_button = S.driver.find_elements(By.CSS_SELECTOR,'[data-testid="like"]')
        liked_or_not = like_button[pos].get_attribute("aria-label")
        if "liked" not in liked_or_not.lower():
            like_button[pos].click()
        
            return True
        else:
            print("Tweet was already like")
        return False
    except Exception as e:
        if is_tweet_exist(S,url) == False:
            print("Tweet don't exist , like error")
        else:
            print("Like error")
        return False


def unlike_a_tweet(S,url):
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
        
        element = WebDriverWait(S.driver,15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="unlike"]'))
        )

        like_button = S.driver.find_elements(By.CSS_SELECTOR,'[data-testid="unlike"]')
        liked_or_not = like_button[pos].get_attribute("aria-label")
        if "liked" in liked_or_not.lower():
            like_button[pos].click()
        else:
            print("tweet was already unlike")
            return False
        
    except Exception as e:
        if is_tweet_exist(S,url) == False:
            print("Tweet don't exist , unlike error")
        else:
            print("Unlike error")
        return False
    
def check_if_tweet_liked(S,url):
    try:
        S.driver.get(url)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="like"]')))
        
        like_button = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="like"]')
        
        liked_or_not = like_button.get_attribute("aria-label")

        if liked_or_not.lower() == "like":
            return False
        else:
            return True
    except Exception as e:
        print("Like error")
        