from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import  *
from src.util.list import *

import time
import traceback

def is_tweet_exist(selenium_session,url):
    try:
        selenium_session.driver.get(url)
        element = WebDriverWait(selenium_session.driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
        return True
    except Exception as e:
        return False
  
def get_tweet_info(selenium_session,url):
    tweet_info_dict = {"username":"",
    "text":"",
    "id":0,
    "date":"",
    "like":0,
    "retweet":0,
    "quote":0,
    "bookmark":0,
    "view":0}
    
    nb_like = 0
    nb_rt = 0
    nb_quote = 0
    nb_bookmark = 0
    nb_view = 0
    try:
        selenium_session.driver.get(url)
        user_tweet = url.split("/")[3]
        
        element = WebDriverWait(selenium_session.driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')))
        tweet_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
        pos = 0
        for i in range(len(tweet_info)):
            r = tweet_info[i]
            if url.split("twitter.com")[1] in str(r.get_attribute("outerHTML")):
                pos = i
                break
        
        element = WebDriverWait(selenium_session.driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))        
        
        
        _tweet_data = selenium_session.driver.find_elements(By.CSS_SELECTOR,'[data-testid="tweet"]')
        _tweet_text = selenium_session.driver.find_elements(By.CSS_SELECTOR,'[data-testid="tweetText"]')
        
        tweet_data = str(_tweet_data[pos].text).split("\n")
        tweet_text = str(_tweet_text[pos].text)
        
        try:
            tweet_date = str(str(tweet_data).split("Translate Tweet")[1]).split(",")[1] + str(str(tweet_data).split("Translate Tweet")[1]).split(",")[2] 
            if "PM" not in tweet_date and "AM" not in tweet_date:
                tweet_date = get_elems_from_list(tweet_data,"AM","PM")
        except:
            try:
                tweet_date = str(str(tweet_data).split(tweet_text)[1]).split(",")[1] + str(str(tweet_data).split(tweet_text)[1]).split(",")[2]
                if "PM" not in tweet_date and "AM" not in tweet_date:
                    tweet_date = get_elems_from_list(tweet_data,"AM","PM")
            except:
                tweet_date = get_elems_from_list(tweet_data,"AM","PM")
        if "Likes" in str(tweet_data):
            nb_like = tweet_data[tweet_data.index(" Likes") - 1]
        if "Bookmarks" in str(tweet_data):
            nb_bookmark = tweet_data[tweet_data.index(" Bookmarks") - 1]
        if "Quotes" in str(tweet_data):
            nb_quote = tweet_data[tweet_data.index(" Quotes") - 1]
        if "Retweets" in str(tweet_data):
            nb_rt = tweet_data[tweet_data.index(" Retweets") - 1]
        if "Views" in str(tweet_data):
            nb_view = tweet_data[tweet_data.index(" Views") - 1]
        
        tweet_info_dict = {"username":tweet_data[1],
        "text":tweet_text,
        "id":int(url.split("status/")[1]),
        "date":tweet_date,
        "like":parse_number(nb_like),
        "retweet":parse_number(nb_rt),
        "quote":parse_number(nb_quote),
        "bookmark":parse_number(nb_bookmark),
        "view":parse_number(nb_view)}
        return (tweet_info_dict)
    except Exception as e:
        if is_tweet_exist(selenium_session,url) == False:
            print("Tweet don't exist , info error")
        else: 
            print("Tweet info error")
        return (tweet_info_dict)

