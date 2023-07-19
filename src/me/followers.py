from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import *
from src.util.list import *
from src.user.info import get_user_info

import time
import traceback
import yaml

with open("configuration.yml", "r") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
        
username_info = str(data["account_username"][0]).replace("@","")

def get_list_of_my_followers(S):
    try:
        nb_of_followers = get_user_info(S,username_info)["follower_count"]
        S.driver.get("https://twitter.com/"+username_info+"/followers")
        run  = True
        list_of_user = []
        selenium_data = []
        account = ""
        nb = 0
        while run:
            try:
                element = WebDriverWait(S.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="UserCell"]')))
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
                            nb+=1
                            time.sleep(0.025)
                        except:
                            time.sleep(0.025)
                            pass
                        if nb >= nb_of_followers:
                            print("Your followers listing done")
                            return(list_of_user)
            except Exception as e:
                print("Your followers listing failed")
                traceback.print_exc()
                return (list_of_user)
        return(list_of_user)
    except Exception as e:
        print("Your followers listing failed")
        traceback.print_exc()
        return([])

def get_list_of_my_followings(S):
    try:
        nb_of_followings = get_user_info(S,username_info)["following_count"]
        S.driver.get("https://twitter.com/"+username_info+"/following")
        run  = True
        list_of_user = []
        selenium_data = []
        account = ""
        nb = 0
        while run:
            try:
                element = WebDriverWait(S.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="UserCell"]')))
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
                            nb+=1
                            time.sleep(0.025)
                        except:
                            time.sleep(0.025)
                            pass
                        if nb >= nb_of_followings:
                            print("Your following listing done")
                            return(list_of_user)
            except Exception as e:
                print("Your following listing failed")
                return (list_of_user)
        return(list_of_user)
    except Exception as e:
        print("Your following listing failed")
        traceback.print_exc()
        return([])
