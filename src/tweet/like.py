from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def like_a_tweet(S,url):
    try:
        S.driver.get(url)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="like"]')))
        
        like_button = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="like"]')
        
        liked_or_not = like_button.get_attribute("aria-label")

        if liked_or_not.lower() == "like":
            like_button.click()
        else:
            print("Tweet already liked")
    except Exception as e:
        print("Like error")
        


def unlike_a_tweet(S,url):
    try:
        S.driver.get(url)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="unlike"]')))
        
        like_button = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="unlike"]')
        
        liked_or_not = like_button.get_attribute("aria-label")

        
        if liked_or_not.lower() == "liked":
            like_button.click()
        else:
            print("Tweet already unliked")
    except Exception as e:
        print("Unlike error")
        