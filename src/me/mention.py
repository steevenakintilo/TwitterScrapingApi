from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import *
from src.util.list import *

import time
import traceback

import yaml

with open("configuration.yml", "r") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
        
username_info = data["account_username"]

def get_mention_url_and_text(S,nb_of_mention):
    try:
        nb = 0
        S.driver.get("https://twitter.com/notifications/mentions")
        run  = True
        list_of_mention_url = []
        big_list = []
        list_of_mention_text = []
        selenium_data = []
        p = '"'
        account = ""
        while run:
            try:
                element = WebDriverWait(S.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
                tweets_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
                tweets_username = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="User-Name"]')
                tweets_text = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweetText"]')
                last_tweet = tweets_info[len(tweets_info) - 1]
                for tweet_info, tweet_username , tweet_text in zip(tweets_info, tweets_username,tweets_text):
                    if tweet_info not in selenium_data:
                        account = str(str(tweet_username.text).split("\n")[1]).replace("@","")
                        account = str(account).lower()
                        lower_data = str(tweet_info.get_property('outerHTML')).lower()
                        
                        splinter = "href="+p+"/"+account+"/status"
                        splinter = splinter.replace("\\","/")                    
                        lower_data = lower_data.split(splinter)

                        lower_data = str(lower_data[1])
                        lower_data = lower_data.split(" ")
                        tweet_id = lower_data[0].replace("/","").replace(p,"")
                        tweet_link = "https://twitter.com/" + account + "/status/" + tweet_id
                        
                        if tweet_link not in list_of_mention_url:
                            list_of_mention_url.append(tweet_link)
                            list_of_mention_text.append(tweet_text.text)
                        selenium_data.append(tweet_info)
                        if len(list_of_mention_url) > nb_of_mention:
                            run = False
                            print("Listing mention end")
                            return(list_of_mention_url,list_of_mention_text)
                big_list.append(last_tweet)
                if are_last_x_elements_same(big_list,200) == True:
                    run = False
                S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                time.sleep(0.05)
            except Exception as e:
                print("You don't have enough mention")
                return (list_of_mention_url,list_of_mention_text)
        print("Listing mention end")
        return(list_of_mention_url)
    except Exception as e:
        print("Error feetching mention")
        return([],[])
