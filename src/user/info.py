from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import *
from src.util.list import *
import time

def _get_user_info(S,user,info):
    try:
        if info == "media":
            S.driver.get("https://twitter.com/"+user+"/media")
            info = "primaryColumn"
        elif info == "like":
            S.driver.get("https://twitter.com/"+user+"/likes")
            info = "primaryColumn"
        else:   
            S.driver.get("https://twitter.com/"+user)
        
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="'+info+'"]')))
                
        elem = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="'+info+'"]')
        
        elem = elem.text
        return (elem)
    except Exception as e:
        print(info , " error")

def get_user_username(S,user):
    username = _get_user_info(S,user,"UserName")
    username = username.split("\n")[0]
    return(username)

def get_user_bio(S,user):
    bio = _get_user_info(S,user,"UserDescription")
    return(bio)

def get_user_date_account_create(S,user):
    date = _get_user_info(S,user,"UserBirthdate")
    return(date)

def get_user_number_of_tweet(S,user):
    tweet = _get_user_info(S,user,"primaryColumn")
    tweet.split("\n")[1]
    tweet = tweet.split("Tweets")
    nb_of_tweet = str(tweet[0]).split("\n")
    return(parse_number(nb_of_tweet[1]))
    
def get_user_number_of_media(S,user):
    nb_of_media = _get_user_info(S,user,"media")
    nb_of_media.split("\n")[1]
    nb_of_media = nb_of_media.split("Photos & videos")
    nb_of_media = str(nb_of_media[0]).split("\n")
    return(parse_number(nb_of_media[1]))
    
def get_user_number_of_like(S,user):
    nb_of_like = _get_user_info(S,user,"like")
    nb_of_like.split("\n")[1]
    nb_of_like = nb_of_like.split("Likes")
    nb_of_like = str(nb_of_like[0]).split("\n")
    return(parse_number(nb_of_like[1]))

def get_user_nb_of_follower(S,user):
    nb_of_follower = _get_user_info(S,user,"primaryColumn").split("\n")
    nb_of_follower = get_elem_from_list(nb_of_follower,"Followers").split(" ")[0]
    return(parse_number(str(nb_of_follower)))

def get_user_nb_of_following(S,user):
    nb_of_following = _get_user_info(S,user,"primaryColumn").split("\n")
    nb_of_following = get_elem_from_list(nb_of_following,"Following").split(" ")[0]
    return(parse_number(str(nb_of_following)))
