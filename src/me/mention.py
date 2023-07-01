from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import *
from src.util.list import *

import time
import traceback

import yaml

with open("configuration.yml", "r") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
        
username_info = data["account_username"]

def get_mention(S):
    try:
        S.driver.get("https://twitter.com/notifications/mentions")
        mention_url = []
        mention_text = []
        mention_formated_text = []
        try:
            for i in range(1,21):
                xpath_mention = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div/div/div["+ str(i) + "]"
                element = WebDriverWait(S.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, xpath_mention)))
                mention_text.append(S.driver.find_element(By.XPATH,xpath_mention).text)
                mention = S.driver.find_element(By.XPATH,xpath_mention)
                mention.click()
                new_url = S.driver.current_url
                mention_url.append(new_url)
                mention_formated_text.append(mention_text[-1].split(str(username_info[0]))[1])
                S.driver.back()
            return (mention_url,mention_formated_text)
        except Exception as e:
            return (mention_url,mention_formated_text)
    except Exception as e:
        print("Mention Error")
        return([],[])
    