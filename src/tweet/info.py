from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import  *

import time

def get_tweet_info(S,url):
    tweet_info = {"username":"",
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
        S.driver.get(url)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))        
        
        tweet_data = str(S.driver.find_element(By.CSS_SELECTOR,'[data-testid="tweet"]').text).split("\n")
        tweet_text = str(S.driver.find_element(By.CSS_SELECTOR,'[data-testid="tweetText"]').text)
        #tweet_date = str(S.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[4]/div/div[1]/div/div[1]/a/time').text)
        tweet_date = ""
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
        
        tweet_info = {"username":tweet_data[1],
        "text":tweet_text,
        "id":int(url.split("status/")[1]),
        "date":tweet_date,
        "like":parse_number(nb_like),
        "retweet":parse_number(nb_rt),
        "quote":parse_number(nb_quote),
        "bookmark":parse_number(nb_bookmark),
        "view":parse_number(nb_view)}
        return (tweet_info)
    except Exception as e:
        print("Tweet info error")
        print(e)
        return (tweet_info)