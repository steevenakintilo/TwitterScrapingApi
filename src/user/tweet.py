from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import *
from src.util.list import *
from src.user.info import get_user_info
from src.tweet.comment import *
from src.util.string import convert_string_to_date

from src.util.list import are_last_x_elements_same , check_elem_on_a_list
from src.user.type import *
import time

import traceback

def get_list_of_user_tweet(selenium_session,account,nb_of_tweet_to_search=100):
    try:
        account = account.replace("@","")
        nb = 0
        #nb_of_tweet = int(get_user_info(selenium_session,account)["tweet_count"])
        if nb_of_tweet_to_search > 3000:
            nb_of_tweet_to_search = nb_of_tweet_to_search - 1
        selenium_session.driver.get("https://twitter.com/"+account)
        run  = True
        selenium_data = []
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
        x = 0
        flop = 0
        if nb_of_tweet_to_search > 3000:
            nb_of_tweet_to_search = 3000
        while run:
            element = WebDriverWait(selenium_session.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
            tweets_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
            tweets_text = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweetText"]')
            last_tweet = tweets_info[len(tweets_info) - 1]
            for tweet_info, tweet_text in zip(tweets_info, tweets_text):
                if are_last_x_elements_same(list_len,250) == True:
                    run = False
                list_len.append(len(data_list))
                
                if len(data_list) >= nb_of_tweet_to_search:
                    run = False
                if tweet_info not in selenium_data:
                    #print("ooo " , tweet_info.text ," ooo")
                    try:
                        #text_list = [text.text.replace("\n"," ").lower() for text in tweets_text]
                        lower_data = str(tweet_info.get_property('outerHTML')).lower()
                        text_ = tweet_text.text.replace("Show more","")
                        if "@" in text_:
                            get_text = str(tweet_info.get_property('outerHTML')).lower().split("css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
                            get_text = get_text[4].split("<")
                            get_text = get_text[0].replace("\n"," ")
                            get_text = get_text[2:len(get_text)]
                            text_list = [text.text.replace("\n"," ").lower() for text in tweets_text]
                            text_ = check_elem_on_a_list(get_text,text_list)
                            #print("tot " , str(tweet_text.text).replace("\n", " "))
                        #get_info = str(tweet_info.get_property('outerHTML')).lower()
                        splinter = "href="+p+"/"+account+"/status"
                        splinter = splinter.replace("\\","/")
                        
                        lower_data = lower_data.split(splinter)
                        lower_data = str(lower_data[1])
                        lower_data = lower_data.split(" ")
                        tweet_id = lower_data[0].replace("/","").replace(p,"")
                        tweet_link = "https://twitter.com/" + account + "/status/" + tweet_id
                        if tweet_id[len(tweet_id) - 1] in "0123456789": 
                            get_like = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("likes")[0]).split(" ")
                            get_like = get_like[len(get_like) - 2]
                            get_reply = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("replies")[0]).split(" ")
                            get_reply = get_reply[len(get_reply) - 2]
                            get_date = str(str(str(str(str(tweet_info.get_property('outerHTML')).lower()).split("datetime")[1]).split(" ")[0]).split(".000z")[0]).replace("t"," ").replace("=","")
                            nb_of_like = get_like.replace("aria-label=","")
                            get_rt = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("retweets")[0]).split(" ")
                            get_rt = get_rt[len(get_rt) - 2]
                            nb_of_rt = get_rt.replace("aria-label=","")
                            nb_of_reply = get_reply.replace("aria-label=","").replace(p,"")
                            if get_rt == ".5-.22.5-.5l19":
                                get_rt = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("retweet")[0]).split(" ")
                                get_rt = get_rt[len(get_rt) - 2]
                            if get_like == ".5-.22.5-.5l19":
                                get_like = str(str(str(tweet_info.get_property('outerHTML')).lower()).split("like")[0]).split(" ")
                                get_like = get_rt[len(get_like) - 2]
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

                        selenium_session.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                        time.sleep(0.025)
                    except Exception as e:
                        try:
                            lower_data = str(tweet_info.get_property('outerHTML')).lower()
                            text_ = tweet_text.text.replace("Show more","")
                            if "@" in text_:
                                get_text = str(tweet_info.get_property('outerHTML')).lower().split("css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
                                get_text = get_text[4].split("<")
                                get_text = get_text[0].replace("\n"," ")
                                get_text = get_text[2:len(get_text)]
                                text_list = [text.text.replace("\n"," ").lower() for text in tweets_text]
                                text_ = check_elem_on_a_list(get_text,text_list)
                                
                                
                                #print("tot " , str(tweet_text.text).replace("\n", " "))
                            
                            splinter = "href=" + p + "/"
                            lower_data = lower_data.split(splinter)
                            user = lower_data[5]
                            user = user.split(p)
                            tweet_stuff = user[0]
                            tweet_link = "https://twitter.com/" + tweet_stuff
                            
                            user_to_check = tweet_stuff.split("/")[0]
                            if user_to_check.lower() == account.lower():
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
                            selenium_session.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.025)
                        except Exception as e:
                            time.sleep(0.1)
        
        if len(data_list) > nb_of_tweet_to_search:
            for i in range(0,nb_of_tweet_to_search):
                list_of_tweet_url_.append(data_list[i])
            return(list_of_tweet_url_)

        else:
            return (data_list)
        

    except Exception as e:
        if is_account_banned(selenium_session,account) == True:
            print("Account is banned error feetching " + account + " tweet")
        elif is_account_existing(selenium_session,account) == True:
            print("Account don't exist error feetching " + account + " tweet")
        elif is_account_blocking_you(selenium_session,account) == True:
            print("Account is blocking you error feetching " + account + " tweet")
        else:
            print("Error feetching " + account + " tweet")
        return(data_list)

def get_list_of_user_retweet(selenium_session,account,nb_of_tweet_to_search=100):
    try:
        account = account.replace("@","")
        nb = 0
        nb_of_tweet = int(get_user_info(selenium_session,account)["tweet_count"])
        if nb_of_tweet_to_search < 3000 and nb_of_tweet_to_search >= nb_of_tweet:
            nb_of_tweet_to_search = nb_of_tweet_to_search - 1
        selenium_session.driver.get("https://twitter.com/"+account)
        run  = True
        list_of_tweet_url = []
        list_of_rt_url = []
        list_of_tweet_url_ = []
        selenium_data = []
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
        flop = 0
        if nb_of_tweet_to_search > 3000:
            nb_of_tweet_to_search = 3000
        while run:
            element = WebDriverWait(selenium_session.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
            tweets_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
            tweets_text = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweetText"]')
            last_tweet = tweets_info[len(tweets_info) - 1]
            for tweet_info, tweet_text in zip(tweets_info, tweets_text):
                if are_last_x_elements_same(list_len,250) == True:
                    run = False
                list_len.append(len(data_list))                
                if len(data_list) >= nb_of_tweet_to_search:
                    run = False
                if len(data_list) >= 3000:
                    run = False
                if tweet_info not in selenium_data:
                    try:
                        lower_data = str(tweet_info.get_property('outerHTML')).lower()
                        text_ = tweet_text.text.replace("Show more","")
                        if "@" in text_:
                            get_text = str(tweet_info.get_property('outerHTML')).lower().split("css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
                            get_text = get_text[4].split("<")
                            get_text = get_text[0].replace("\n"," ")
                            get_text = get_text[2:len(get_text)]
                            text_list = [text.text.replace("\n"," ").lower() for text in tweets_text]
                            text_ = check_elem_on_a_list(get_text,text_list)
                        
                        splinter = "href=" + p + "/"
                        lower_data = lower_data.split(splinter)
                        user = lower_data[5]
                        user = user.split(p)
                        tweet_stuff = user[0]
                        tweet_link = "https://twitter.com/" + tweet_stuff
                        user_to_check = tweet_stuff.split("/")[0]
                        if user_to_check.lower() != account.lower():
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
                                
                                tweet_info_dict = {"username":user_to_check,"text":text_,"id":int(str(tweet_link.split("status/")[1]).replace("/photo/1","")),"url":tweet_link,"date":str(convert_string_to_date(get_date.replace(p,""))),"like":int(str(nb_of_like).replace(p,"")),"retweet":int(str(nb_of_rt).replace(p,"")),"reply":int(str(nb_of_reply).replace(p,""))}
                                data_list.append(tweet_info_dict)
                        selenium_data.append(tweet_info)
                        selenium_session.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                        time.sleep(0.030)
                    except Exception as e:    
                        time.sleep(0.030)
        
        if len(data_list) > nb_of_tweet_to_search:
            for i in range(0,nb_of_tweet_to_search):
                list_of_tweet_url_.append(data_list[i])
        
            return(list_of_tweet_url_)
        else:
            return (data_list)
    except Exception as e:
        if is_account_banned(selenium_session,account) == True:
            print("Account is banned error feetching " + account + " retweet")
        elif is_account_existing(selenium_session,account) == True:
            print("Account don't exist error feetching " + account + " retweet")
        elif is_account_blocking_you(selenium_session,account) == True:
            print("Account is blocking you error feetching " + account + " retweet")
        else:
            print("Error feetching " + account + " retweet")
        return(data_list)

def get_list_of_user_comment(selenium_session,account,nb_of_tweet_to_search=100):
    try:
        account = account.replace("@","")
        final_list_url = []
        nb = 0
        nb_of_tweet = int(get_user_info(selenium_session,account)["tweet_count"])
        if nb_of_tweet_to_search < 3000 and nb_of_tweet_to_search >= nb_of_tweet:
            nb_of_tweet_to_search = nb_of_tweet_to_search - 1
        selenium_session.driver.get("https://twitter.com/"+account+"/with_replies")
        run  = True
        list_of_tweet_url = []
        selenium_data = []
        list_of_tweet_url_ = []
        final_list_url = []
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
        flop = 0
        if nb_of_tweet_to_search > 3000:
            nb_of_tweet_to_search = 3000
        while run:
            element = WebDriverWait(selenium_session.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
            tweets_info = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
            tweets_text = selenium_session.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweetText"]')
            tweets_text = tweets_text[:-1]
            last_tweet = tweets_info[len(tweets_info) - 1]
            for tweet_info, tweet_text in zip(tweets_info, tweets_text):
                if are_last_x_elements_same(list_len,250) == True:
                    run = False
                list_len.append(len(data_list))                
                if len(data_list) >= nb_of_tweet_to_search:
                    run = False
                if tweet_info not in selenium_data:
                    try:
                        lower_data = str(tweet_info.get_property('outerHTML')).lower()
                        if "useravatar-container-"+account.lower() in lower_data and tweet_text.text.lower() in lower_data:
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

                            if account in  tweet_link and tweet_link not in list_of_tweet_url:
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
                        selenium_session.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                        time.sleep(0.030)
                    except:
                        try:
                            lower_data = str(tweet_info.get_property('outerHTML')).lower()
                            if "useravatar-container-"+account.lower() in lower_data and tweet_text.text.lower() in lower_data:
                                text_ = tweet_text.text.replace("Show more","")
                                if "@" in text_:
                                    get_text = str(tweet_info.get_property('outerHTML')).lower().split("css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
                                    get_text = get_text[4].split("<")
                                    get_text = get_text[0].replace("\n"," ")
                                    get_text = get_text[2:len(get_text)]
                                    text_list = [text.text.replace("\n"," ").lower() for text in tweets_text]
                                    text_ = check_elem_on_a_list(get_text,text_list)
                                
                                splinter = "href=" + p + "/"
                                lower_data = lower_data.split(splinter)
                                user = lower_data[5]
                                user = user.split(p)
                                tweet_stuff = user[0]
                                tweet_link = "https://twitter.com/" + tweet_stuff
                                user_to_check = tweet_stuff.split("/")[0]
                                if user_to_check.lower() == account.lower() and tweet_link not in list_of_tweet_url:
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
                            selenium_session.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.030)
                        except Exception as e:
                            flop = flop + 1
                            time.sleep(0.030)
        
        if len(data_list) > nb_of_tweet_to_search:
            for i in range(0,nb_of_tweet_to_search):
                list_of_tweet_url_.append(data_list[i])
            return(list_of_tweet_url_)
        else:
            return (data_list)
    except Exception as e:
        if is_account_banned(selenium_session,account) == True:
            print("Account is banned error feetching " + account + " comment")
        elif is_account_existing(selenium_session,account) == True:
            print("Account don't exist error feetching " + account + " comment")
        elif is_account_blocking_you(selenium_session,account) == True:
            print("Account is blocking you error feetching " + account + " comment")
        else:
            print("Error feetching " + account + " comment")
        return(data_list)
