from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

def comment_a_tweet(S,url,text):

    try:
        text = str(text)
        S.driver.get(url)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="reply"]')))
        
        comment_button = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="reply"]')
        comment_button.click()

        time.sleep(5)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')))
        
        textbox = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
        textbox.click()
        time.sleep(S.wait_time)
        textbox.send_keys(text)
        
        time.sleep(5)
        
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        wait = WebDriverWait(S.driver, 10)
        target_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        S.driver.execute_script("arguments[0].scrollIntoView();", target_element)

        target_element.click()

        time.sleep(5)
        print("comment done")
    except Exception as e:
        print(e)
        print("comment error")    
