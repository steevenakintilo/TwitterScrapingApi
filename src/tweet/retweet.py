from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

def reetweet_a_tweet(S,url):

    try:
        S.driver.get(url)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="retweet"]')))
        
        reetweet_button = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="retweet"]')
        reetweet_button.click()

        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="retweetConfirm"]')))
        
        reetweet_button = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="retweetConfirm"]')
        reetweet_button.click()
        
        print("reetweet done")
    except Exception as e: 
        print("retweet error")
        print(e)

def unreetweet_a_tweet(S,url):

    try:
        S.driver.get(url)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="unretweet"]')))
        
        unreetweet_button = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="unretweet"]')
        unreetweet_button.click()

        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="unretweetConfirm"]')))
        
        unreetweet_button = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="unretweetConfirm"]')
        unreetweet_button.click()
        
        print("reetweet done")
    except Exception as e: 
        print("retweet error")
        print(e)

def quote_a_tweet(S,url,text):
    
    try:
        S.driver.get("https://twitter.com/compose/tweet")
        time.sleep(10)
        #print("coment part one")
        
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')))
        
        textbox = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
        textbox.click()
        time.sleep(S.wait_time)
        textbox.send_keys(url + " " + text)
        
        time.sleep(5)
        
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        wait = WebDriverWait(S.driver, 10)
        target_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        S.driver.execute_script("arguments[0].scrollIntoView();", target_element)

        target_element.click()
    except Exception as e: 
        print("quote error")
        print(e)