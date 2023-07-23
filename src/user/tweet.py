from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import *
from src.util.list import *
from src.user.info import get_user_info
from src.tweet.comment import *

from src.user.type import *

import time

import traceback

def get_list_of_user_tweet_url(S,account,nb_of_tweet_to_search):
    try:
        account = account.replace("@","")
        nb = 0
        nb_of_tweet = int(get_user_info(S,account)["tweet_count"])
        if nb_of_tweet_to_search < 3000 and nb_of_tweet_to_search >= nb_of_tweet:
            nb_of_tweet_to_search = nb_of_tweet_to_search - 1
        S.driver.get("https://twitter.com/"+account)
        run  = True
        list_of_tweet_url = []
        selenium_data = []
        list_of_tweet_url_ = []
        p = '"'
        flop = 0
        if nb_of_tweet_to_search > 3000:
            nb_of_tweet_to_search = 3000
        while run:
            element = WebDriverWait(S.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
            tweets_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
            last_tweet = tweets_info[len(tweets_info) - 1]
            for tweet_info in tweets_info:
                if len(list_of_tweet_url) >= nb_of_tweet_to_search:
                    run = False
                if tweet_info not in selenium_data:
                    try:
                        lower_data = str(tweet_info.get_property('outerHTML')).lower()
                        if "something went wrong. Try reloading" in lower_data:
                            #tweet_info.click()
                            lower_data.click()
                            time.sleep(0.1)
                        
                        splinter = "href="+p+"/"+account+"/status"
                        splinter = splinter.replace("\\","/")
                        
                        lower_data = lower_data.split(splinter)
                        lower_data = str(lower_data[1])
                        lower_data = lower_data.split(" ")
                        tweet_id = lower_data[0].replace("/","").replace(p,"")
                        tweet_link = "https://twitter.com/" + account + "/status/" + tweet_id
                                            
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
                            user = lower_data[5]
                            user = user.split(p)
                            tweet_stuff = user[0]
                            tweet_link = "https://twitter.com/" + tweet_stuff
                            user_to_check = tweet_stuff.split("/")[0]
                            if user_to_check.lower() == account.lower():
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
        if is_account_banned(S,user) == True:
            print("Account is banned error feetching " + account + " tweet")
        elif is_account_existing(S,user) == True:
            print("Account don't exist error feetching " + account + " tweet")
        elif is_account_blocking_you(S,user) == True:
            print("Account is blocking you error feetching " + account + " tweet")
        else:
            print("Error feetching " + account + " tweet")
        return(list_of_tweet_url)


def get_list_of_user_rt_url(S,account,nb_of_tweet_to_search):
    try:
        account = account.replace("@","")
        nb = 0
        nb_of_tweet = int(get_user_info(S,account)["tweet_count"])
        if nb_of_tweet_to_search < 3000 and nb_of_tweet_to_search >= nb_of_tweet:
            nb_of_tweet_to_search = nb_of_tweet_to_search - 1
        S.driver.get("https://twitter.com/"+account)
        run  = True
        list_of_tweet_url = []
        list_of_rt_url = []
        list_of_tweet_url_ = []
        selenium_data = []

        p = '"'
        flop = 0
        if nb_of_tweet_to_search > 3000:
            nb_of_tweet_to_search = 3000
        while run:
            element = WebDriverWait(S.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
            tweets_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
            last_tweet = tweets_info[len(tweets_info) - 1]
            for tweet_info in tweets_info:
                if len(list_of_rt_url) >= nb_of_tweet_to_search:
                    run = False
                if len(list_of_tweet_url) >= 3000:
                    run = False
                if tweet_info not in selenium_data:
                    try:
                        lower_data = str(tweet_info.get_property('outerHTML')).lower()
                        if "something went wrong. Try reloading" in lower_data:
                            lower_data.click()
                            time.sleep(0.1)
                        
                        splinter = "href="+p+"/"+account+"/status"
                        splinter = splinter.replace("\\","/")
                        
                        lower_data = lower_data.split(splinter)
                        lower_data = str(lower_data[1])
                        lower_data = lower_data.split(" ")
                        tweet_id = lower_data[0].replace("/","").replace(p,"")
                        tweet_link = "https://twitter.com/" + account + "/status/" + tweet_id
                        list_of_tweet_url.append(tweet_link)            
                        selenium_data.append(tweet_info)
                        S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                        time.sleep(0.025)
                    except:
                        try:
                            lower_data = str(tweet_info.get_property('outerHTML')).lower()
                            if "something went wrong. Try reloading" in lower_data:
                                lower_data.click()
                                time.sleep(0.1)
                            
                            splinter = "href=" + p + "/"
                            lower_data = lower_data.split(splinter)
                            user = lower_data[5]
                            user = user.split(p)
                            tweet_stuff = user[0]
                            tweet_link = "https://twitter.com/" + tweet_stuff
                            user_to_check = tweet_stuff.split("/")[0]
                            if user_to_check.lower() != account.lower():
                                list_of_rt_url.append(tweet_link)
                                list_of_tweet_url.append(tweet_link)
                            selenium_data.append(tweet_info)
                            S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.030)
                        except Exception as e:    
                            time.sleep(0.030)
        
        if len(list_of_rt_url) > nb_of_tweet_to_search:
            for i in range(0,nb_of_tweet_to_search):
                list_of_tweet_url_.append(list_of_rt_url[i])
        
            return(list_of_tweet_url_)
        else:
            return (list_of_rt_url)
    except Exception as e:
        if is_account_banned(S,user) == True:
            print("Account is banned error feetching " + account + " retweet")
        elif is_account_existing(S,user) == True:
            print("Account don't exist error feetching " + account + " retweet")
        elif is_account_blocking_you(S,user) == True:
            print("Account is blocking you error feetching " + account + " retweet")
        else:
            print("Error feetching " + account + " retweet")
        return(list_of_rt_url)




def get_list_of_user_comment_url(S,account,nb_of_tweet_to_search):
    try:
        account = account.replace("@","")
        final_list_url = []
        nb = 0
        nb_of_tweet = int(get_user_info(S,account)["tweet_count"])
        if nb_of_tweet_to_search < 3000 and nb_of_tweet_to_search >= nb_of_tweet:
            nb_of_tweet_to_search = nb_of_tweet_to_search - 1
        S.driver.get("https://twitter.com/"+account+"/with_replies")
        run  = True
        list_of_tweet_url = []
        selenium_data = []
        list_of_tweet_url_ = []
        final_list_url = []

        p = '"'
        flop = 0
        if nb_of_tweet_to_search > 3000:
            nb_of_tweet_to_search = 3000
        while run:
            element = WebDriverWait(S.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
            tweets_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
            last_tweet = tweets_info[len(tweets_info) - 1]
            for tweet_info in tweets_info:
                if len(list_of_tweet_url) >= nb_of_tweet_to_search:
                    run = False
                    print("totototototototo")
                if tweet_info not in selenium_data:
                    try:
                        lower_data = str(tweet_info.get_property('outerHTML')).lower()
                        if "something went wrong. Try reloading" in lower_data:
                            lower_data.click()
                            time.sleep(0.1)
                        splinter = "href="+p+"/"+account+"/status"
                        splinter = splinter.replace("\\","/")
                        
                        lower_data = lower_data.split(splinter)
                        lower_data = str(lower_data[1])
                        lower_data = lower_data.split(" ")
                        tweet_id = lower_data[0].replace("/","").replace(p,"")
                        tweet_link = "https://twitter.com/" + account + "/status/" + tweet_id

                        if account in  tweet_link and tweet_link not in list_of_tweet_url:                
                            list_of_tweet_url.append(tweet_link)
                        selenium_data.append(tweet_info)
                        S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                        time.sleep(0.030)
                    except:
                        try:
                            lower_data = str(tweet_info.get_property('outerHTML')).lower()
                            if "something went wrong. Try reloading" in lower_data:
                                #tweet_info.click()
                                lower_data.click()
                                time.sleep(0.1)
                            
                            splinter = "href=" + p + "/"
                            lower_data = lower_data.split(splinter)
                            user = lower_data[5]
                            user = user.split(p)
                            tweet_stuff = user[0]
                            tweet_link = "https://twitter.com/" + tweet_stuff
                            user_to_check = tweet_stuff.split("/")[0]
                            if user_to_check.lower() == account.lower() and tweet_link not in list_of_tweet_url:
                                list_of_tweet_url.append(tweet_link)
                            selenium_data.append(tweet_info)
                            S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.030)
                        except Exception as e:    
                            flop = flop + 1
                            time.sleep(0.030)
        
        if len(list_of_tweet_url) > nb_of_tweet_to_search:
            for i in range(0,nb_of_tweet_to_search):
                list_of_tweet_url_.append(list_of_tweet_url[i])
            return(list_of_tweet_url_)
        else:
            return (list_of_tweet_url)
    except Exception as e:
        if is_account_banned(S,user) == True:
            print("Account is banned error feetching " + account + " comment")
        elif is_account_existing(S,user) == True:
            print("Account don't exist error feetching " + account + " comment")
        elif is_account_blocking_you(S,user) == True:
            print("Account is blocking you error feetching " + account + " comment")
        else:
            print("Error feetching " + account + " comment")
        return(list_of_tweet_url)
