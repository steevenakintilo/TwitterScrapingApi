from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import pyperclip

from src.util.string import *
import time

def make_a_tweet(S,text="",media=False,filepath=""):
    try:
        if len(text) == 0 or len(text) > 240:
            print("Text lenght must be between 1 and 240")
            return ("")

        S.driver.get("https://twitter.com/compose/tweet")
        time.sleep(1.5)
        
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')))
        
        textbox = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
        textbox.click()
        time.sleep(1.5)
                
        pyperclip.copy(text)
        act = ActionChains(S.driver)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

        if media == True:
            file_input = S.driver.find_element(By.XPATH,"//input[@type='file']")
            file_input.send_keys(filepath)
        
        time.sleep(1.5)
        
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        wait = WebDriverWait(S.driver, 10)
        target_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        S.driver.execute_script("arguments[0].scrollIntoView();", target_element)

        target_element.click()
        time.sleep(1.5)
        
    except Exception as e:
        if "File not found" in str(e):
            print("Can't tweet file not found")
        elif "Message: invalid argument: 'text' is empty" in str(e):
            print("Media set to true nbut no media added")
        else:
            print(e)
            print("tweet error")


def make_a_tweet_with_poll(S,text="",nb_of_choice=2,choice1_text="1",choice2_text="2",choice3_text="3",choice4_text="4",days=1,hours=0,minutes=0):
    try:
        if len(text) == 0:
            text = "."
        if len(text) == 0 or len(text) > 280:
            text = text[0:279]
               
        if len(choice1_text) > 25:
            choice1_text = choice1_text[0:24]
        if len(choice2_text) > 25:
            choice2_text = choice2_text[0:24]
        if len(choice3_text) > 25:
            choice3_text = choice3_text[0:24]
        if len(choice4_text) > 25:
            choice4_text = choice4_text[0:24]
        
        if len(choice1_text) == 0:
            choice1_text = "."
        if len(choice2_text) == 0:
            choice2_text = "."
        if len(choice3_text) == 0:
            choice3_text = "."
        if len(choice4_text) == 0:
            choice4_text = "."
        
        if nb_of_choice > 4:
            nb_of_choice = 4
        if nb_of_choice < 2:
            nb_of_choice = 2
            choice2_text = "."
        
        S.driver.get("https://twitter.com/compose/tweet")
        time.sleep(1.5)
        
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0RichTextInputContainer"]')))
        
        textbox = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0RichTextInputContainer"]')
        textbox.click()
        time.sleep(1.5)
        
        pyperclip.copy(text)
        act = ActionChains(S.driver)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

        time.sleep(1.5)
        
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="createPollButton"]')))

        poll_btn = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="createPollButton"]')
        poll_btn.click()

        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="addPollChoice"]')))
        
        for i in range(nb_of_choice - 2):
            add_pool = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="addPollChoice"]')
            add_pool.click()
            
        if nb_of_choice == 2:
            choice1 = S.driver.find_element(By.NAME, "Choice1")
            S.driver.execute_script("arguments[0].scrollIntoView();", choice1)
            choice1.click()
            pyperclip.copy(choice1_text)
            act = ActionChains(S.driver)
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

            choice2 = S.driver.find_element(By.NAME, "Choice2")
            S.driver.execute_script("arguments[0].scrollIntoView();", choice2)
            choice2.click()
            pyperclip.copy(choice2_text)
            act = ActionChains(S.driver)
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
            
        if nb_of_choice == 3:            
            choice1 = S.driver.find_element(By.NAME, "Choice1")
            S.driver.execute_script("arguments[0].scrollIntoView();", choice1)
            choice1.click()
            pyperclip.copy(choice1_text)
            act = ActionChains(S.driver)
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

            choice2 = S.driver.find_element(By.NAME, "Choice2")
            S.driver.execute_script("arguments[0].scrollIntoView();", choice2)
            choice2.click()
            pyperclip.copy(choice2_text)
            act = ActionChains(S.driver)
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

            choice3 = S.driver.find_element(By.NAME, "Choice3")
            S.driver.execute_script("arguments[0].scrollIntoView();", choice3)
            choice3.click()
            pyperclip.copy(choice3_text)
            act = ActionChains(S.driver)
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

        if nb_of_choice == 4:
            choice1 = S.driver.find_element(By.NAME, "Choice1")
            S.driver.execute_script("arguments[0].scrollIntoView();", choice1)
            choice1.click()
            pyperclip.copy(choice1_text)
            act = ActionChains(S.driver)
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

            choice2 = S.driver.find_element(By.NAME, "Choice2")
            S.driver.execute_script("arguments[0].scrollIntoView();", choice2)
            choice2.click()
            pyperclip.copy(choice2_text)
            act = ActionChains(S.driver)
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

            choice3 = S.driver.find_element(By.NAME, "Choice3")
            S.driver.execute_script("arguments[0].scrollIntoView();", choice3)
            choice3.click()
            pyperclip.copy(choice3_text)
            act = ActionChains(S.driver)
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

            choice4 = S.driver.find_element(By.NAME, "Choice4")
            S.driver.execute_script("arguments[0].scrollIntoView();", choice4)
            choice4.click()
            pyperclip.copy(choice4_text)
            act = ActionChains(S.driver)
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        
        if days > 6:
            days = 7
        elif days < 0:
            days = 0
        else:
            days = days - 1

        if hours > 23:
            hours = 23
        elif hours < 0:
            hours = 0
        if minutes > 59:
            days = 59
        elif minutes < 5:
            minutes = 5
        else:
            minutes - 1        
        days_ =  S.driver.find_element(By.CSS_SELECTOR, '[data-testid="selectPollDays"]')
        S.driver.execute_script("arguments[0].scrollIntoView();", days_)
        days_.click()
        for i in range(days):
            days_.send_keys(Keys.ARROW_DOWN)
        days_.send_keys(Keys.RETURN)
        
        if days <= 0:
            days_.click()
            days_.send_keys(Keys.ARROW_UP)
            days_.send_keys(Keys.RETURN)
        

        hours_ =  S.driver.find_element(By.CSS_SELECTOR, '[data-testid="selectPollHours"]')
        S.driver.execute_script("arguments[0].scrollIntoView();", hours_)
        hours_.click()
        
        if hours <= 0:
            hours_.click()
            hours_.send_keys(Keys.ARROW_UP)
            hours_.send_keys(Keys.RETURN)

        if days >= 1 and days < 7:
            hours_.click()
            for i in range(hours):
                hours_.send_keys(Keys.ARROW_DOWN)
            hours_.send_keys(Keys.RETURN)

            minutes_ =  S.driver.find_element(By.CSS_SELECTOR, '[data-testid="selectPollMinutes"]')
            S.driver.execute_script("arguments[0].scrollIntoView();", minutes_)
            minutes_.click()
            
            for i in range(minutes):
                minutes_.send_keys(Keys.ARROW_DOWN)
            minutes_.send_keys(Keys.RETURN)
            minutes_.click()
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))
        
        wait = WebDriverWait(S.driver, 10)
        target_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        S.driver.execute_script("arguments[0].scrollIntoView();", target_element)

        target_element.click()
        time.sleep(1.5)
        
    except Exception as e:
        print("Tweet with pool error")

def delete_a_tweet(S,url):
    try:
        S.driver.get(url)
        time.sleep(1.5)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="caret"]')))
        optionbox = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="caret"]')
        optionbox.click()
        time.sleep(0.1)
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="Dropdown"]')))
        wait = WebDriverWait(S.driver, 10)
        target_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="Dropdown"]')))
        tweet_option = str(target_element.text).split("\n")
        if tweet_option[0] == "Delete":
            element = WebDriverWait(S.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div[1]')))
            element.click()
            element = WebDriverWait(S.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="confirmationSheetConfirm"]')))
            element.click()
            time.sleep(0.5)
            return True
        else:
            print("You can't delete another person tweet")
            return False 
        
    except Exception as e:
        print("Tweet delete error")
        return False


def bookmark_a_tweet(S,url):
    try:
        S.driver.get(url)
        time.sleep(1.5)
        pos = 0
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')))
        
        tweet_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
        for i in range(len(tweet_info)):
            r = tweet_info[i]
            if url.split("twitter.com")[1] in str(r.get_attribute("outerHTML")):
                pos = i
                break
        try:
            element = WebDriverWait(S.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="bookmark"]')))
            bookmark_btn = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="bookmark"]')

            bookmark_btn[pos].click()
            time.sleep(0.1)
        except:
            pass            
    except Exception as e:
        print(e)
        print("Tweet bookmark error")

def unbookmark_a_tweet(S,url):
    try:
        S.driver.get(url)
        time.sleep(1.5)
        pos = 0
        element = WebDriverWait(S.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')))
        
        tweet_info = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
        for i in range(len(tweet_info)):
            r = tweet_info[i]
            if url.split("twitter.com")[1] in str(r.get_attribute("outerHTML")):
                pos = i
                break
        try:
            element = WebDriverWait(S.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="removebookmark"]')))
            bookmark_btn = S.driver.find_elements(By.CSS_SELECTOR, '[data-testid="removebookmark"]')

            bookmark_btn[pos].click()
            time.sleep(0.1)
        except:
            pass            
    except Exception as e:
        print(e)
        print("Tweet unbookmark error")