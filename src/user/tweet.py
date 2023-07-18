from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.util.num import *
from src.util.list import *
import time
from bs4 import BeautifulSoup

def get_user_tweet(S,user):
    try:
        #S.driver.get("https://twitter.com/"+user)
        S.driver.get("https://twitter.com/search?q=cambodge&src=typed_query&f=live")
        tweet_url = []
        page_source = S.driver.page_source

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(page_source, "html.parser")
        print(soup.text.strip())
        # Find the desired element using soup.find()
        elements = soup.find_all('p', attrs={"data-testid": "tweetText"})

        # Print the result
        #print(element)
        for element in elements:
            print(element.text.strip())
        time.sleep(1000)

        for i in range(1,20):
            #a = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div/div/div["+str(i)+"]/div/div/article/div/div/div[2]/div[2]/div[2]/div"
            #a = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div/div/div["+str(i)+"]/div/div/article/div/div/div[2]/div[2]/div[2]/div/span[1]"
            a = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div/div/div["+str(i)+"]/div/div/article/div/div"
            element = WebDriverWait(S.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, a)))
            elem = S.driver.find_element(By.XPATH, a)
            #elem = elem.text
            elem.click()
            new_url = S.driver.current_url
            tweet_url.append(new_url)
            S.driver.back()
            print(elem)
            print("test")
            #a = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div[2]/div"
            #b = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div/div/div[9]/div/div/article/div/div/div[2]/div[2]/div[2]/div"
            #print(elem)
            #for element in elem:
            #     element_text = element.text
            #     print(element_text)
            #     print(len(elem))
            #     print("coco")
        return ("caca")
    except Exception as e:
        print(e)
        print("User Tweet error")

