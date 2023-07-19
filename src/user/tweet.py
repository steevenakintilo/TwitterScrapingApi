from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import *
from src.util.list import *
import time

import traceback

def get_list_of_tweet_user_url(S,account,nb_of_tweet_to_search):
    try:
        nb = 0
        S.driver.get("https://twitter.com/"+account+"/with_replies")
        run  = True
        list_of_tweet_url = []
        selenium_data = []
        p = '"'
        while run:
            element = WebDriverWait(S.driver, 300).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
            tweets_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
            last_tweet = tweets_info[len(tweets_info) - 1]
            for tweet_info in tweets_info:
                if tweet_info not in selenium_data:
                    lower_data = str(tweet_info.get_property('outerHTML')).lower()
                    
                    splinter = "href="+p+"/"+account+"/status"
                    splinter = splinter.replace("\\","/")
                    
                    lower_data = lower_data.split(splinter)
                    lower_data = str(lower_data[1])
                    lower_data = lower_data.split(" ")
                    tweet_id = lower_data[0].replace("/","").replace(p,"")
                    tweet_link = "https://twitter.com/" + account + "/status/" + tweet_id
                    
                    print("##### link: " + tweet_link , " nb of tweet found: " , len(list_of_tweet_url) , " #####")
                    
                    list_of_tweet_url.append(tweet_link)
                    selenium_data.append(tweet_info)
                    if len(list_of_tweet_url) > nb_of_tweet_to_search:
                        run = False
            S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
            time.sleep(0.05)
        return(list_of_tweet_url)
        print("Listing tweet end")
    except Exception as e:
        print("Error feetching " + account + " tweet")
        traceback.print_exc()
        return([])
