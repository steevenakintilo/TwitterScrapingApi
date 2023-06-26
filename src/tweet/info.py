from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def parse_number(num):
    if "B" in num:
        if "." in num:
            num  = num.replace(".","").replace("B","")
            num  = num + "00000000"
            
        else:
            num = num.replace("B","")
            num  = num + "000000000"
            
    elif "M" in num:
        if "." in num:
            num  = num.replace(".","").replace("B","")
            num  = num + "00000"

        else:
            num = num.replace("B","")
            num  = num + "000000"
    
    elif "K" in num:
        if "." in num:
            num  = num.replace(".","").replace("K","")
            num = num + "00"
        else:
            num = num.replace("K","")
            num = num + "000"
    else:
        if "." in num:
            num  = num.replace(".","").replace("B","")
        else:
            num = num.replace("B","")
    if "," in num:
        num = num.replace(",")
    return num

def get_tweet_data(S,url,info):
    try:
        S.driver.get(url)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))        
        tweet_data = str(S.driver.find_element(By.CSS_SELECTOR,'[data-testid="tweet"]').text).split("\n")
        if info == " Text":
            return tweet_data[2]
        if info == " User":
            return tweet_data[1]
        if info not in str(tweet_data):
            return 0
        number_of_bookmark = tweet_data[tweet_data.index(info) - 1]
        return (number_of_bookmark)
    except Exception as e:
        if info == " Text":
            print("Get text error")
            return ("")
        if info == " User":
            print("Get user error")
            return ("")
        print("Tweet number of " + info + "error")
        return (0)

def get_tweet_nb_of_like(S,url):
    number_of_like = parse_number(get_tweet_data(S,url," Likes"))
    return number_of_like

def get_tweet_nb_of_retweet(S,url):
    number_of_rt = parse_number(get_tweet_data(S,url," Retweets"))
    return number_of_rt


def get_tweet_nb_of_quote(S,url):
    number_of_quote = parse_number(get_tweet_data(S,url," Quotes"))
    return number_of_quote


def get_tweet_nb_of_view(S,url):
    number_of_view = parse_number(get_tweet_data(S,url," Views"))
    return number_of_view

def get_tweet_nb_of_bookmark(S,url):
    number_of_bookmark = parse_number(get_tweet_data(S,url," Bookmarks"))
    return number_of_bookmark


def get_tweet_user(S,url):
    tweet_user = get_tweet_data(S,url," User")
    return tweet_user

def get_tweet_text(S,url):
    tweet_text = get_tweet_data(S,url," Text")
    return tweet_text
