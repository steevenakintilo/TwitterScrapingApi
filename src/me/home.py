from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import *
from src.util.list import *
from src.user.info import get_user_info
from src.tweet.comment import *

from src.util.list import are_last_x_elements_same

from src.user.type import *

import time

import traceback

def get_list_of_homepage_tweet_url(S,nb_of_tweet_to_search):
    try:
        nb = 0
        S.driver.get("https://twitter.com/home")
        run  = True
        list_of_tweet_url = []
        selenium_data = []
        list_len = []
        list_of_tweet_url_ = []
        p = '"'
        flop = 0
        if nb_of_tweet_to_search > 100:
            nb_of_tweet_to_search = 100
        while run:
            element = WebDriverWait(S.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
            tweets_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
            last_tweet = tweets_info[len(tweets_info) - 1]
            for tweet_info in tweets_info:
                if are_last_x_elements_same(list_len,500) == True:
                    run = False
                list_len.append(len(list_of_tweet_url))
                if len(list_of_tweet_url) >= nb_of_tweet_to_search:
                    run = False
                if tweet_info not in selenium_data:
                    try:
                        lower_data = str(tweet_info.get_property('outerHTML')).lower()
                        if "something went wrong. Try reloading" in lower_data:
                            #tweet_info.click()
                            lower_data.click()
                            time.sleep(0.1)
                        splinter = "href=" + p + "/"
                        lower_data = lower_data.split(splinter)
                        user = lower_data[4]
                        user = user.split(p)
                        tweet_stuff = user[0]
                        tweet_link = "https://twitter.com/" + tweet_stuff
                        user_to_check = tweet_stuff.split("/")[0]
                        list_of_tweet_url.append(tweet_link)
                        selenium_data.append(tweet_info)
                        S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                        time.sleep(0.025)
                    except:
                        try:
                            lower_data = str(tweet_info.get_property('outerHTML')).lower()
                            if "something went wrong. Try reloading" in lower_data:
                                #tweet_info.click()
                                lower_data.click()
                                time.sleep(0.1)
                            splinter = "href=" + p + "/"
                            lower_data = lower_data.split(splinter)
                            user = lower_data[4]
                            user = user.split(p)
                            tweet_stuff = user[0]
                            tweet_link = "https://twitter.com/" + tweet_stuff
                            user_to_check = tweet_stuff.split("/")[0]
                            list_of_tweet_url.append(tweet_link)
                            selenium_data.append(tweet_info)
                            S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.025)
                        except Exception as e:    
                            time.sleep(0.1)
        

        if len(list_of_tweet_url) > nb_of_tweet_to_search:
            for i in range(0,nb_of_tweet_to_search):
                list_of_tweet_url_.append(list_of_tweet_url[i])
            return(list_of_tweet_url_)

        else:
            return (list_of_tweet_url) 

    except Exception as e:
        print("Error feetching homepage")
        return(list_of_tweet_url)
