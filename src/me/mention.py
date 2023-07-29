from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import *
from src.util.list import *
from src.util.list import check_elem_on_a_list
from src.util.string import convert_string_to_date
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
                        
                        if tweet_link[len(tweet_link) - 1] in "0123456789" and "status" in tweet_link and tweet_link not in list_of_mention_url:
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
                        if len(data_list) > nb_of_mention:
                            run = False
                            print("Listing mention end")
                            return(data_list)
                big_list.append(last_tweet)
                if are_last_x_elements_same(big_list,200) == True:
                    run = False
                S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                time.sleep(0.05)
            except Exception as e:
                print("You don't have enough mention")
                return (data_list)
        
        if len(data_list) > nb_of_mention:
            for i in range(0,nb_of_mention):
                list_of_tweet_url_.append(data_list[i])
            return(list_of_tweet_url_)
        else:
            return (data_list)        
    except Exception as e:
        print("Error feetching mention")
        return(data_list)
