from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import traceback
import time
def search_tweet(S,query="hello",mode="toto",nb_of_tweet_to_search=100):
    list_of_tweet_url = []
    selenium_data = []
    list_of_tweet_url_ = []
    
    try:
        nb = 0
        #if nb_of_tweet_to_search < 3000 and nb_of_tweet_to_search >= nb_of_tweet:
        #    nb_of_tweet_to_search = nb_of_tweet_to_search - 1
        if mode == "top":
            S.driver.get("https://twitter.com/search?q="+query+"&src=typed_query&f=top")
        elif mode == "recent":
            S.driver.get("https://twitter.com/search?q="+query+"&src=typed_query&f=live")
        else:
            S.driver.get("https://twitter.com/search?q="+query+"&src=typed_query&f=live")
        
        run  = True
        p = '"'
        flop = 0
        #if nb_of_tweet_to_search > 3000:
        #    nb_of_tweet_to_search = 3000
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
                        
                        splinter = "href=" + p + "/"
                        lower_data = lower_data.split(splinter)
                        user = lower_data[5]
                        user = user.split(p)
                        tweet_stuff = user[0]
                        tweet_link = "https://twitter.com/" + tweet_stuff
                        print(tweet_stuff)
                        print(tweet_link)
                        time.sleep(100000)
                                        
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
                            list_of_tweet_url.append(tweet_link)
                            selenium_data.append(tweet_info)
                            S.driver.execute_script("arguments[0].scrollIntoView();", last_tweet)
                            time.sleep(0.030)
                        except Exception as e:    
                            flop = flop + 1
                            time.sleep(0.1)
        

        if len(list_of_tweet_url) > nb_of_tweet_to_search:
            for i in range(0,nb_of_tweet_to_search):
                list_of_tweet_url_.append(list_of_tweet_url[i])
            return(list_of_tweet_url_)

        else:
            return (list_of_tweet_url)
        

        print("Searching tweet end")
    except Exception as e:
        print("Error searching " + query + " tweet")
        traceback.print_exc()
        return(list_of_tweet_url)
