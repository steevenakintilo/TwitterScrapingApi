from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.list import are_last_x_elements_same
from src.tweet.info import *
import time
import traceback


def get_list_of_user_who_like_a_tweet(S,url,nb_of_like):
    try:
        nb = 0
        S.driver.get(url+"/likes")
        run  = True
        list_of_user = []
        selenium_data = []
        account = ""
        list_len = []
        flop = 0
        if nb_of_like > 2000:
            nb_of_like = 2000
        while run:
            try:
                element = WebDriverWait(S.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="UserCell"]')))
                tweets_username = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="UserCell"]')
                last_user = tweets_username[len(tweets_username) - 1]
                for tweet_username in tweets_username:
                    if are_last_x_elements_same(list_len,100) == True:
                        run = False
                    list_len.append(len(list_of_user))
                    if tweet_username not in selenium_data:
                        try:
                            parsing_user = str(tweet_username.text).split("\n")
                            account = parsing_user[1]

                            list_of_user.append(account.replace("@",""))
                            selenium_data.append(tweet_username)
                            S.driver.execute_script("arguments[0].scrollIntoView();", tweet_username)
                            time.sleep(0.025)
                        except Exception as e:
                            time.sleep(0.025)
                        
                        if len(list_of_user) >= nb_of_like:
                            run = False
                            return(list_of_user)
            except Exception as e:
                return (list_of_user)
        return(list_of_user)
    except Exception as e:
        if is_tweet_exist(S,url) == False:
            print("Tweet don't exist , can't feetch user who liked this tweet")
        else:
            print("Error feetching user who liked this tweet")
        return([])


def get_list_of_user_who_retweet_a_tweet(S,url,nb_of_rt):
    try:
        nb = 0
        S.driver.get(url+"/retweets")
        run  = True
        list_of_user = []
        selenium_data = []
        list_len = []
        p = '"'
        account = ""
        if nb_of_rt > 2000:
            nb_of_rt = 2000
        while run:
            try:
                element = WebDriverWait(S.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="UserCell"]')))
                tweets_username = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="UserCell"]')
                last_user = tweets_username[len(tweets_username) - 1]
                for tweet_username in tweets_username:
                    if are_last_x_elements_same(list_len,100) == True:
                        run = False
                    list_len.append(len(list_of_user))
                    if tweet_username not in selenium_data:
                        try:
                            parsing_user =str(tweet_username.text).split("\n")
                            account = parsing_user[1]
                            list_of_user.append(account.replace("@",""))
                            selenium_data.append(tweet_username)
                            S.driver.execute_script("arguments[0].scrollIntoView();", tweet_username)
                            time.sleep(0.025)
                        except:
                            time.sleep(0.025)
                            pass
                        if len(list_of_user) >= nb_of_rt:
                            run = False
                            return(list_of_user)
            except Exception as e:
                return (list_of_user)
        print("zzzzz")
        return(list_of_user)
    except Exception as e:
        if is_tweet_exist(S,url) == False:
            print("Tweet don't exist , can't feetch user who retweeted this tweet")
        else:
            print("Error feetching user who retweeted this tweet")
        
        return([])


def get_list_of_quote_of_a_tweet(S,url,nb_of_quote):
    try:
        nb = 0
        S.driver.get(url+"/retweets/with_comments")
        time.sleep(1)
        run  = True
        list_of_quote_url = []
        selenium_data = []
        p = '"'
        account = ""
        list_len = []
        if nb_of_quote > 100:
            nb_of_quote = 100

        while run:
            try:
                element = WebDriverWait(S.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
                tweets_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
                tweets_username = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="User-Name"]')
                last_tweet = tweets_info[len(tweets_info) - 1]
                for tweet_info, tweet_username in zip(tweets_info, tweets_username):
                    if are_last_x_elements_same(list_len,100) == True:
                        run = False
                    list_len.append(len(list_of_quote_url))
                    if tweet_info not in selenium_data:
                        try:
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
                            if tweet_link not in list_of_quote_url:
                                if tweet_link[len(tweet_link) - 1] in "0123456789" and "status" in tweet_link:
                                    list_of_quote_url.append(tweet_link)
                            selenium_data.append(tweet_info)
                            S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.025)
                        except:
                            S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.1)
                        if len(list_of_quote_url) >= nb_of_quote:
                            run = False
                            return(list_of_quote_url)
                        
            except Exception as e:
                return (list_of_quote_url)
        return(list_of_quote_url)
    except Exception as e:
        if is_tweet_exist(S,url) == False:
            print("Tweet don't exist , can't get list of quote of this tweet")
        else:
            print("Error feetching list of quote of this tweet")
        
        return([])


def get_list_of_comment_of_a_tweet(S,url,nb_of_comment):
    try:
        nb = 0
        S.driver.get(url)
        time.sleep(1)
        run  = True
        list_of_comment_url = []
        selenium_data = []
        p = '"'
        account = ""
        list_len = []
        if nb_of_comment > 250:
            nb_of_comment = 250

        while run:
            try:
                element = WebDriverWait(S.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
                tweets_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
                tweets_username = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="User-Name"]')
                last_tweet = tweets_info[len(tweets_info) - 1]
                for tweet_info, tweet_username in zip(tweets_info, tweets_username):
                    if are_last_x_elements_same(list_len,500) == True:
                        run = False
                    list_len.append(len(list_of_comment_url))
                    if tweet_info not in selenium_data:
                        try:
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
                            if tweet_link not in list_of_comment_url:
                                if tweet_link[len(tweet_link) - 1] in "0123456789" and "status" in tweet_link:
                                    list_of_comment_url.append(tweet_link)
                            selenium_data.append(tweet_info)
                            S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.025)
                        except:
                            S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.1)
                        if len(list_of_comment_url) >= nb_of_comment:
                            run = False
                            return(list_of_comment_url)
                        
            except Exception as e:
                return (list_of_comment_url)
        return(list_of_comment_url)
    except Exception as e:
        print(is_tweet_exist(S,url))

        if is_tweet_exist(S,url) == False:
            print("Tweet don't exist , can't get list of comment of this tweet")
        else:
            print("Error feetching list of comment of this tweet")
        return([])