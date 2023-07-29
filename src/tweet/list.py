from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.list import are_last_x_elements_same
from src.tweet.info import *

from src.util.string import convert_string_to_date
from src.util.list import are_last_x_elements_same , check_elem_on_a_list
from src.user.type import *

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
        data_list = []
        list_of_tweet_url_ = []
        text_list = []
        tweet_info_dict = {"username":"",
        "text":"",
        "id":0,
        "url":"",
        "date":"",
        "like":0,
        "retweet":0,
        "reply":0,}
        
        if nb_of_quote > 100:
            nb_of_quote = 100

        while run:
            try:
                element = WebDriverWait(S.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
                tweets_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
                tweets_username = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="User-Name"]')
                tweets_text = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweetText"]')
                last_tweet = tweets_info[len(tweets_info) - 1]
                for tweet_info, tweet_username, tweet_text in zip(tweets_info, tweets_username,tweets_text):
                    if are_last_x_elements_same(list_len,100) == True:
                        run = False
                    list_len.append(len(list_of_quote_url))
                    if tweet_info not in selenium_data:
                        try:
                            account = str(str(tweet_username.text).split("\n")[1]).replace("@","")
                            account = str(account).lower()
                            lower_data = str(tweet_info.get_property('outerHTML')).lower()
                            text_ = tweet_text.text.replace("Show more","")
                            if "@" in text_:
                                get_text = str(tweet_info.get_property('outerHTML')).lower().split("css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
                                get_text = get_text[4].split("<")
                                get_text = get_text[0].replace("\n"," ")
                                get_text = get_text[2:len(get_text)]
                                text_list = [text.text.replace("\n"," ").lower() for text in tweets_text]
                                text_ = check_elem_on_a_list(get_text,text_list)
                            
                            splinter = "href="+p+"/"+account+"/status"
                            splinter = splinter.replace("\\","/")                    
                            lower_data = lower_data.split(splinter)
                            lower_data = str(lower_data[1])
                            lower_data = lower_data.split(" ")
                            tweet_id = lower_data[0].replace("/","").replace(p,"")
                            tweet_link = "https://twitter.com/" + account + "/status/" + tweet_id
                            if tweet_link not in list_of_quote_url:
                                if tweet_link[len(tweet_link) - 1] in "0123456789" and "status" in tweet_link:
                                    get_like = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("likes")[0]).split(" ")
                                    get_like = get_like[len(get_like) - 2]
                                    get_reply = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("replies")[0]).split(" ")
                                    get_reply = get_reply[len(get_reply) - 2]
                                    get_date = str(str(str(str(str(tweet_info.get_property('outerHTML')).lower()).split("datetime")[1]).split(" ")[0]).split(".000z")[0]).replace("t"," ").replace("=","")
                                    nb_of_like = get_like.replace("aria-label=","")
                                    get_rt = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("retweets")[0]).split(" ")
                                    get_rt = get_rt[len(get_rt) - 2]
                                    nb_of_rt = 0
                                    nb_of_reply = get_reply.replace("aria-label=","").replace(p,"")
                                    if get_rt == ".5-.22.5-.5l19":
                                        get_rt = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("retweet")[0]).split(" ")
                                        get_rt = get_rt[len(get_rt) - 2]
                                    if get_like == ".5-.22.5-.5l19":
                                        get_like = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("like")[0]).split(" ")
                                        get_like = get_like[len(get_like) - 2]        
                                    if get_reply == ".5-.22.5-.5l19":
                                        get_reply = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("reply")[0]).split(" ")
                                        get_reply = get_reply[len(get_reply) - 2]     
                                    if get_like.isnumeric() == True:
                                        nb_of_like = parse_number(get_like)
                                    if get_rt.isnumeric() == True:
                                        nb_of_rt = parse_number(get_rt)                                    
                                    if get_reply.isnumeric() == True:
                                        nb_of_reply = parse_number(get_reply)                            
                                    
                                    tweet_info_dict = {"username":account,"text":text_,"id":int(str(tweet_link.split("status/")[1]).replace("/photo/1","")),"url":tweet_link,"date":str(convert_string_to_date(get_date.replace(p,""))),"like":int(str(nb_of_like).replace(p,"")),"retweet":int(str(nb_of_rt).replace(p,"")),"reply":int(str(nb_of_reply).replace(p,""))}
                                    data_list.append(tweet_info_dict)
                            selenium_data.append(tweet_info)
                            S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.025)
                        except:
                            S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.1)
                        if len(data_list) >= nb_of_quote:
                            run = False
                            return(data_list)
                    if len(data_list) > nb_of_quote:
                        for i in range(0,nb_of_quote):
                            list_of_tweet_url_.append(data_list[i])       
                        return(list_of_tweet_url_)
            
            except Exception as e:
                return (data_list)
        return(data_list)
    except Exception as e:
        if is_tweet_exist(S,url) == False:
            print("Tweet don't exist , can't get list of quote of this tweet")
        else:
            print("Error feetching list of quote of this tweet")
        
        return(data_list)


def get_list_of_comment_of_a_tweet(S,url,nb_of_comment=10):
    try:
        nb = 0
        if nb_of_comment > 0:
            nb_of_comment = nb_of_comment + 1
        S.driver.get(url)
        time.sleep(1)
        run  = True
        selenium_data = []
        list_of_comment_url = []
        list_of_tweet_url_ = []
        list_len = []
        data_list = []
        text_list = []
        tweet_info_dict = {"username":"",
        "text":"",
        "id":0,
        "url":"",
        "date":"",
        "like":0,
        "retweet":0,
        "reply":0,}
        
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
                tweets_text = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweetText"]')
                last_tweet = tweets_info[len(tweets_info) - 1]
                for tweet_info, tweet_username, tweet_text in zip(tweets_info, tweets_username,tweets_text):
                    if are_last_x_elements_same(list_len,500) == True:
                        run = False
                    list_len.append(len(data_list))
                    if tweet_info not in selenium_data:
                        try:
                            account = str(str(tweet_username.text).split("\n")[1]).replace("@","")
                            account = str(account).lower()
                            lower_data = str(tweet_info.get_property('outerHTML')).lower()
                            
                            text_ = tweet_text.text.replace("Show more","")
                            if "@" in text_:
                                get_text = str(tweet_info.get_property('outerHTML')).lower().split("css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
                                get_text = get_text[4].split("<")
                                get_text = get_text[0].replace("\n"," ")
                                get_text = get_text[2:len(get_text)]
                                text_list = [text.text.replace("\n"," ").lower() for text in tweets_text]
                                text_ = check_elem_on_a_list(get_text,text_list)
                            
                            splinter = "href="+p+"/"+account+"/status"
                            splinter = splinter.replace("\\","/")                    
                            lower_data = lower_data.split(splinter)
                            lower_data = str(lower_data[1])
                            lower_data = lower_data.split(" ")
                            tweet_id = lower_data[0].replace("/","").replace(p,"")
                            tweet_link = "https://twitter.com/" + account + "/status/" + tweet_id
                            if "photo1" in tweet_link and "/photo" not in tweet_link:
                                tweet_link = tweet_link.replace("photo1","/photo1")
                            if tweet_link not in list_of_comment_url:
                                if tweet_link[len(tweet_link) - 1] in "0123456789" and "status" in tweet_link:
                                    get_like = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("likes")[0]).split(" ")
                                    get_like = get_like[len(get_like) - 2]
                                    get_reply = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("replies")[0]).split(" ")
                                    get_reply = get_reply[len(get_reply) - 2]
                                    get_date = str(str(str(str(str(tweet_info.get_property('outerHTML')).lower()).split("datetime")[1]).split(" ")[0]).split(".000z")[0]).replace("t"," ").replace("=","")
                                    nb_of_like = get_like.replace("aria-label=","")
                                    get_rt = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("retweets")[0]).split(" ")
                                    get_rt = get_rt[len(get_rt) - 2]
                                    nb_of_rt = 0
                                    nb_of_reply = get_reply.replace("aria-label=","").replace(p,"")
                                    if get_rt == ".5-.22.5-.5l19":
                                        get_rt = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("retweet")[0]).split(" ")
                                        get_rt = get_rt[len(get_rt) - 2]
                                    if get_like == ".5-.22.5-.5l19":
                                        get_like = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("like")[0]).split(" ")
                                        get_like = get_like[len(get_like) - 2]        
                                    if get_reply == ".5-.22.5-.5l19":
                                        get_reply = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("reply")[0]).split(" ")
                                        get_reply = get_reply[len(get_reply) - 2]     
                                    if get_like.isnumeric() == True:
                                        nb_of_like = parse_number(get_like)
                                    if get_rt.isnumeric() == True:
                                        nb_of_rt = parse_number(get_rt)                                    
                                    if get_reply.isnumeric() == True:
                                        nb_of_reply = parse_number(get_reply)                            
                                    
                                    tweet_info_dict = {"username":account,"text":text_,"id":int(str(tweet_link.split("status/")[1]).replace("/photo/1","")),"url":tweet_link,"date":str(convert_string_to_date(get_date.replace(p,""))),"like":int(str(nb_of_like).replace(p,"")),"retweet":int(str(nb_of_rt).replace(p,"")),"reply":int(str(nb_of_reply).replace(p,""))}
                                    data_list.append(tweet_info_dict)
                            selenium_data.append(tweet_info)
                            S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.025)
                        except:
                            S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.1)
                        
                        if len(data_list) >= nb_of_comment:
                            run = False
                            return(data_list)
                if len(data_list) > 0:
                    data_list = data_list[1:]
                if len(data_list) > nb_of_comment:
                    for i in range(0,nb_of_comment):
                        list_of_tweet_url_.append(data_list[i])
                
                    return(list_of_tweet_url_)
        
            except Exception as e:
                return (data_list)
        return(data_list)
    except Exception as e:
        print(is_tweet_exist(S,url))

        if is_tweet_exist(S,url) == False:
            print("Tweet don't exist , can't get list of comment of this tweet")
        else:
            print("Error feetching list of comment of this tweet")
        return(data_list)