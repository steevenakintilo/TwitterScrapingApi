from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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
        if nb_of_like > 5000:
            nb_of_like = 5000
        while run:
            try:
                element = WebDriverWait(S.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="UserCell"]')))
                #tweets_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
                tweets_username = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="UserCell"]')
                last_user = tweets_username[len(tweets_username) - 1]
                for tweet_username in tweets_username:
                
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
                        if len(list_of_user) > nb_of_like:
                            run = False
                            print("Listing tweet like end")
                            return(list_of_user)
            except Exception as e:
                return (list_of_user)
        print("Listing tweet like end")
        return(list_of_user)
    except Exception as e:
        print("Error feetching tweet like")
        traceback.print_exc()
        return([])


def get_list_of_user_who_retweet_a_tweet(S,url,nb_of_rt):
    try:
        nb = 0
        S.driver.get(url+"/retweets")
        run  = True
        list_of_user = []
        selenium_data = []
        p = '"'
        account = ""
        if nb_of_rt > 5000:
            nb_of_rt = 5000
        while run:
            try:
                element = WebDriverWait(S.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="UserCell"]')))
                #tweets_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
                tweets_username = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="UserCell"]')
                last_user = tweets_username[len(tweets_username) - 1]
                for tweet_username in tweets_username:
                
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
                        if len(list_of_user) > nb_of_rt:
                            run = False
                            print("Listing tweet like end")
                            return(list_of_user)
            except Exception as e:
                return (list_of_user)
        print("Listing tweet like end")
        return(list_of_user)
    except Exception as e:
        print("Error feetching tweet like")
        traceback.print_exc()
        return([])


def get_list_of_quote_of_a_tweet(S,url,nb_of_quote):
    try:
        nb = 0
        S.driver.get(url+"/retweets/with_comments")
        time.sleep(1)
        run  = True
        list_of_quote_url = []
        list_of_quote_text = []
        selenium_data = []
        p = '"'
        account = ""
        if nb_of_quote > 30:
            nb_of_quote = 30

        while run:
            try:
                element = WebDriverWait(S.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
                tweets_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
                tweets_username = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="User-Name"]')
                last_tweet = tweets_info[len(tweets_info) - 1]
                for tweet_info, tweet_username in zip(tweets_info, tweets_username):
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
                                print("##### link: " , tweet_link , " ##### "  , len(list_of_quote_url))
                                list_of_quote_url.append(tweet_link)
                            selenium_data.append(tweet_info)
                            time.sleep(0.05)
                        except:
                            print("floooop")
                            time.sleep(0.05)
                        if len(list_of_quote_url) > nb_of_quote:
                            run = False
                            print("Listing mention end")
                            return(list_of_quote_url)
                        
                S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                time.sleep(0.05)
            except Exception as e:
                print("jojojoj")
                print(len(list_of_quote_url))
                print("cacacaca")
                traceback.print_exc()
                return (list_of_quote_url)
        print("Listing tweet quote end")
        return(list_of_quote_url)
    except Exception as e:
        print("Error feetching tweet quote")
        traceback.print_exc()
        return([])
