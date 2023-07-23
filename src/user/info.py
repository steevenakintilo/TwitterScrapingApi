from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import *
from src.util.list import *

from src.user.type import *

import time
import traceback

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
        if is_account_banned(S,user) == True:
            print("Account is banned retrieving user info error")
        elif is_account_existing(S,user) == True:
            print("Account don't exist banned retrieving user info error")
        elif is_account_blocking_you(S,user) == True:
            print("Account is blocking you retrieving user info error")
        else:
            print("Error while retrieving user info")
        return("")
def get_user_info(S,user):
    user_info = {"username":"",
    "bio":"",
    "birthdate":"",
    "tweet_count":0,
    "follower_count":0,
    "following_count":0}
    try:
        S.driver.get("https://twitter.com/"+user)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="UserName"]')))
        
        username = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="UserName"]').text
        bio = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="UserDescription"]').text
        try:
            birthdate = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="UserBirthdate"]').text
        except:
            birthdate = "None"
        tweet_count = parse_number(str(str(S.driver.find_element(By.CSS_SELECTOR, '[data-testid="primaryColumn"]').text.split("\n")[1]).split("\n")[0]).split(" ")[0])
        follower_count = parse_number(get_elem_from_list(S.driver.find_element(By.CSS_SELECTOR, '[data-testid="primaryColumn"]').text.split("\n"),"Followers").split(" ")[0])
        try:
            following_count = parse_number(get_elem_from_list_special(S.driver.find_element(By.CSS_SELECTOR, '[data-testid="primaryColumn"]').text.split("\n"),"Following").split(" ")[0])
        except:
            following_count = parse_number(get_elem_from_list(S.driver.find_element(By.CSS_SELECTOR, '[data-testid="primaryColumn"]').text.split("\n"),"Following").split(" ")[0])
        user_info = {"username":username,
        "bio":bio,
        "birthdate":birthdate,
        "tweet_count":tweet_count,
        "follower_count":follower_count,
        "following_count":following_count}
        return (user_info)
    except Exception as e:
        if is_account_banned(S,user) == True:
            print("Account is banned user info error")
        elif is_account_existing(S,user) == True:
            print("Account don't exist user info error")
        elif is_account_blocking_you(S,user) == True:
            print("Account is blocking you user info error")
        else:
            print("User info error")
        return(user_info)

def get_user_number_of_media(S,user):
    try:
        nb_of_media = _get_user_info(S,user,"media")
        nb_of_media.split("\n")[1]
        nb_of_media = nb_of_media.split("Photos & videos")
        nb_of_media = str(nb_of_media[0]).split("\n")
        return(parse_number(nb_of_media[1]))
    except:
        
        if is_account_banned(S,user) == True:
            print("Account is banned user number of media error")
        elif is_account_existing(S,user) == True:
            print("Account is banned user number of media error")
        elif is_account_blocking_you(S,user) == True:
            print("Account is blocking you user number of media error")
        else:
            print("Error while retrieving user number of media")
        return (0)
            
def get_user_number_of_like(S,user):
    try:
        nb_of_like = _get_user_info(S,user,"like")
        nb_of_like.split("\n")[1]
        nb_of_like = nb_of_like.split("Likes")
        nb_of_like = str(nb_of_like[0]).split("\n")
        return(parse_number(nb_of_like[1]))
    except:
        if is_account_banned(S,user) == True:
            print("Account is banned user number of like error")
        elif is_account_existing(S,user) == True:
            print("Account is banned user number of like error")
        elif is_account_blocking_you(S,user) == True:
            print("Account is blocking you user number of like error")
        else:
            print("Error while retrieving user number of like")
        
        return(0)