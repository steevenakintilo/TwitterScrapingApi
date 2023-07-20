from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import *
from src.util.list import *
from src.user.info import get_user_info
from src.tweet.comment import is_tweet_a_comment

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
                            splinter = "href=" + p + "/"
                            lower_data = lower_data.split(splinter)
                            user = lower_data[5]
                            user = user.split(p)
                            tweet_stuff = user[0]
                            tweet_link = "https://twitter.com/" + tweet_stuff
                            if user_to_check.lower() == account.lower():
                                list_of_tweet_url.append(tweet_link)
                            selenium_data.append(tweet_info)
                            S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.025)
                        except Exception as e:    
                            flop = flop + 1
                            print("flop " , flop)
                            #print("error " , error)
                            time.sleep(0.025)
        return(list_of_tweet_url)
        print("Listing tweet end")
    except Exception as e:
        print("Error feetching " + account + " tweet")
        traceback.print_exc()
        return([])


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
                            time.sleep(0.025)
                        except Exception as e:    
                            flop = flop + 1
                            print("flop " , flop)
                            #print("error " , error)
                            time.sleep(0.025)
        return(list_of_rt_url)
        print("Listing tweet end")
    except Exception as e:
        print("Error feetching " + account + " tweet")
        traceback.print_exc()
        return([])


def get_list_of_user_comment_url(S,account,nb_of_tweet_to_search):
    try:
        account = account.replace("@","")
        nb = 0
        nb_of_tweet = int(get_user_info(S,account)["tweet_count"])
        time.sleep(1000)
        if nb_of_tweet_to_search < 3000 and nb_of_tweet_to_search >= nb_of_tweet:
            nb_of_tweet_to_search = nb_of_tweet_to_search - 1
        S.driver.get("https://twitter.com/"+account+"/with_replies")
        run  = True
        list_of_tweet_url = []
        list_of_comment_url = []
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
                if len(list_of_comment_url) >= nb_of_tweet_to_search:
                    run = False
                if len(list_of_tweet_url) >= 3000:
                    run = False
                if tweet_info not in selenium_data:
                    try:
                        lower_data = str(tweet_info.get_property('outerHTML')).lower()
                        
                        splinter = "href="+p+"/"+account+"/status"
                        splinter = splinter.replace("\\","/")
                        
                        lower_data = lower_data.split(splinter)
                        lower_data = str(lower_data[1])
                        lower_data = lower_data.split(" ")
                        tweet_id = lower_data[0].replace("/","").replace(p,"")
                        tweet_link = "https://twitter.com/" + account + "/status/" + tweet_id
                        if is_tweet_a_comment(S,tweet_link) == True:
                            list_of_comment_url.append(tweet_link)       
                            list_of_tweet_url.append(tweet_link)
                        selenium_data.append(tweet_info)
                        S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                        time.sleep(0.025)
                    except:
                        try:
                            lower_data = str(tweet_info.get_property('outerHTML')).lower()
                            splinter = "href=" + p + "/"
                            lower_data = lower_data.split(splinter)
                            user = lower_data[5]
                            user = user.split(p)
                            tweet_stuff = user[0]
                            tweet_link = "https://twitter.com/" + tweet_stuff
                            if user_to_check.lower() == account.lower():
                                if is_tweet_a_comment(S,tweet_link) == True:
                                    list_of_tweet_url.append(tweet_link)
                                    list_of_comment_url.append(tweet_link)
                            selenium_data.append(tweet_info)
                            S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.025)
                        except Exception as e:    
                            flop = flop + 1
                            print("flop " , flop)
                            #print("error " , error)
                            time.sleep(0.025)
        print("infity" * 10)
        time.sleep(10000)
        return(list_of_comment_url)
        print("Listing tweet end")
    except Exception as e:
        print("Error feetching " + account + " tweet")
        traceback.print_exc()
        return([])
