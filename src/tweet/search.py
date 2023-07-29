from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from src.util.list import are_last_x_elements_same
import traceback
import time

from src.util.string import convert_string_to_date
from src.util.num import *
from src.util.list import are_last_x_elements_same , check_elem_on_a_list


def search_tweet(S,query="hello",mode="recent",nb_of_tweet_to_search=10):
    list_of_tweet_url = []
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
    
    try:
        if mode == "top":
            S.driver.get("https://twitter.com/search?q="+query+"&src=typed_query&f=top")
        elif mode == "recent":
            S.driver.get("https://twitter.com/search?q="+query+"&src=typed_query&f=live")
        else:
            S.driver.get("https://twitter.com/search?q="+query+"&src=typed_query&f=live")
        
        run  = True
        p = '"'
        while run:
            element = WebDriverWait(S.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
            tweets_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
            tweets_text = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweetText"]')
            last_tweet = tweets_info[len(tweets_info) - 1]
            for tweet_info, tweet_text in zip(tweets_info, tweets_text):
                if len(data_list) >= nb_of_tweet_to_search:
                    run = False
                list_len.append(len(data_list))
                if are_last_x_elements_same(list_len,500) == True:
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
                            text_ = "toto"
                            for i in range(len(tweets_text)):
                                try:
                                    text_list.append(tweets_text[i].text)
                                except:
                                    pass
                                
                            #text_list = [text.text.replace("\n"," ").lower() for text in tweets_text]
                            text_ = check_elem_on_a_list(get_text,text_list)
                            text_list = []

                        splinter = "href=" + p + "/"
                        
                        lower_data = lower_data.split(splinter)
                        user = lower_data[4]
                        user = user.split(p)
                        tweet_stuff = user[0]
                        tweet_link = "https://twitter.com/" + tweet_stuff
                        user = tweet_stuff.split("/")[0]
                        tweet_link = tweet_link.replace("/analytics","")
                        if "/status" in tweet_link:
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
                            tweet_info_dict = {"username":user,"text":text_,"id":int(str(tweet_link.split("status/")[1]).replace("/photo/1","")),"url":tweet_link,"date":str(convert_string_to_date(get_date.replace(p,""))),"like":int(str(nb_of_like).replace(p,"")),"retweet":int(str(nb_of_rt).replace(p,"")),"reply":int(str(nb_of_reply).replace(p,""))}
                            data_list.append(tweet_info_dict)
                            #print("list len ", len(list_of_tweet_url))
                        selenium_data.append(tweet_info)
                        
                        S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                        time.sleep(0.030)
                    except:
                        try:
                            lower_data = str(tweet_info.get_property('outerHTML')).lower()
                            text_ = tweet_text.text.replace("Show more","")
                            text_ = tweet_text.text.replace("Show more","")
                            if "@" in text_:
                                get_text = str(tweet_info.get_property('outerHTML')).lower().split("css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
                                get_text = get_text[4].split("<")
                                get_text = get_text[0].replace("\n"," ")
                                get_text = get_text[2:len(get_text)]
                                text_ = "toto"
                                for i in range(len(tweets_text)):
                                    try:                                    
                                        text_list.append(tweets_text[i].text)
                                    except:
                                        pass
                                    
                                #text_list = [text.text.replace("\n"," ").lower() for text in tweets_text]
                                text_ = check_elem_on_a_list(get_text,text_list)
                                text_list = []
                            
                            splinter = "href=" + p + "/"
                            lower_data = lower_data.split(splinter)
                            user = lower_data[5]
                            user = user.split(p)
                            tweet_stuff = user[0]
                            tweet_link = "https://twitter.com/" + tweet_stuff
                            user = tweet_stuff.split("/")[0]
                            if tweet_link[len(tweet_link) - 1] in "0123456789" and "status" in tweet_link:
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
                            tweet_info_dict = {"username":user,"text":text_,"id":int(str(tweet_link.split("status/")[1]).replace("/photo/1","")),"url":tweet_link,"date":str(convert_string_to_date(get_date.replace(p,""))),"like":int(str(nb_of_like).replace(p,"")),"retweet":int(str(nb_of_rt).replace(p,"")),"reply":int(str(nb_of_reply).replace(p,""))}
                            data_list.append(tweet_info_dict)
                            list_of_tweet_url.append(tweet_link)
                        
                            selenium_data.append(tweet_info)                        
                            
                            S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.030)
                        except Exception as e:
                            time.sleep(0.1)
        

        if len(data_list) > nb_of_tweet_to_search:
            for i in range(0,nb_of_tweet_to_search):
                list_of_tweet_url_.append(data_list[i])
            return(list_of_tweet_url_)

        else:
            return (data_list)
    except Exception as e:
        print("Error searching " + query + " tweet")
        traceback.print_exc()
        return(data_list)
