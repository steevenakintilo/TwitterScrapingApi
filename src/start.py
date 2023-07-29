from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from os import system
from selenium.webdriver.common.by import By
from random import randint

import time
import pickle
import yaml
import traceback

class Scraper:
    
    wait_time = 5
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("--log-level=3")  # Suppress all logging levels
    language_code = "en"  # Specify the desired language code (e.g., "en" for English)
    options.add_argument("--lang={}".format(language_code))
    driver = webdriver.Chrome(options=options)  # to open the chromedriver    
    driver.execute_script(f"document.documentElement.lang = '{language_code}';")


    username_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
    
    button_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
    password_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
    login_button_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div'
    cookie_button_xpath = '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]/div/span/span'
    notification_button_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/span/span'
    test_tweet = 'https://twitter.com/Twitter/status/1580661436132757506'
    
    
def login(selenium_session,_username,_password):

    try:
        selenium_session.driver.get("https://twitter.com/i/flow/login")
        print("Starting Twitter")

        #USERNAME
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.XPATH, selenium_session.username_xpath)))

        username = selenium_session.driver.find_element(By.XPATH,selenium_session.username_xpath)
        username.send_keys(_username)    
        
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.XPATH, selenium_session.button_xpath)))


        #FIRST BUTTON

        button = selenium_session.driver.find_element(By.XPATH,selenium_session.button_xpath)
        button.click()
        #print("button click")


        #PASSWORD
        
        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.XPATH, selenium_session.password_xpath)))
        
        password = selenium_session.driver.find_element(By.XPATH,selenium_session.password_xpath)
        password.send_keys(_password)
        #print("password done")


        #LOGIN BUTTON

        element = WebDriverWait(selenium_session.driver, 15).until(
        EC.presence_of_element_located((By.XPATH, selenium_session.login_button_xpath)))
        
        login_button = selenium_session.driver.find_element(By.XPATH,selenium_session.login_button_xpath)
        login_button.click()

        #print("Closing Twitter")
    except Exception as e:
        print("Username wrong change your info on the configuration.yml file")
        quit()

def check_login_good(selenium_session):
    try:
        selenium_session.driver.get("https://twitter.com/home")
        element = WebDriverWait(selenium_session.driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="AppTabBar_Notifications_Link"]')))
        print("Login done")
        return True
    except Exception as e:
        
        print("Password wrong change your info on the configuration.yml file")
        return False
    
def accept_coockie(selenium_session):
    try:
        selenium_session.driver.get(selenium_session.test_tweet)

        element = WebDriverWait(selenium_session.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, selenium_session.cookie_button_xpath)))
        
        cookie_button = selenium_session.driver.find_element(By.XPATH,selenium_session.cookie_button_xpath)
        cookie_button.click()

    except:
        pass    
        
    print("coockie done")


def accept_notification(selenium_session):
    try:
        selenium_session.driver.get(selenium_session.test_tweet)

        element = WebDriverWait(selenium_session.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, selenium_session.notification_button_xpath)))
        
        cookie_button = selenium_session.driver.find_element(By.XPATH,selenium_session.notification_button_xpath)
        cookie_button.click()
    except:
        pass    
    try:
        selenium_session.driver.get(selenium_session.test_tweet)

        element = WebDriverWait(selenium_session.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, selenium_session.cookie_button_xpath)))
        
        cookie_button = selenium_session.driver.find_element(By.XPATH,selenium_session.cookie_button_xpath)
        cookie_button.click()

    except:
        pass    
    
    print("notification done")
    
def check_connection(selenium_session):
    try:
        selenium_session.driver.set_page_load_timeout(30)
        selenium_session.driver.get("https://www.google.com/")
        return True
    except:
        print("No internet connection")
        return False

def save_coockie(selenium_session):
    pickle.dump(selenium_session.driver.get_cookies(), open("cookies.pkl", "wb"))

def print_file_info(path):
    f = open(path, 'rb')
    content = f.read()
    f.close()
    return(str(content))

def start_selenium():
    ELON_MUSK = 20
    ck = print_file_info("cookies.pkl")
    with open("configuration.yml", "r") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    if len(str(ck)) > ELON_MUSK:
        selenium_session = Scraper()
        username_info = data["account_username"]
        print("Connection to" , username_info[0] , "account")
        if check_connection(selenium_session) == False:
            exit()
        selenium_session.driver.get("https://twitter.com/i/flow/login")
        
        cookies = pickle.load(open("cookies.pkl","rb"))

        for cookie in cookies:
            selenium_session.driver.add_cookie(cookie)
        time.sleep(0.2)
        print("Already Connected Nice")
        return (selenium_session)
    else:
        username_info = data["account_username"]
        password_info = data["account_password"]
        
        selenium_session = Scraper()
        print("Connection to" , username_info[0] , "account")
        if check_connection(selenium_session) == False:
            exit()
        login(selenium_session,username_info[0],password_info[0])
        time.sleep(selenium_session.wait_time)
        if check_login_good(selenium_session) == False:
            quit()
        time.sleep(selenium_session.wait_time)
        accept_coockie(selenium_session)
        time.sleep(selenium_session.wait_time)    
        accept_notification(selenium_session)
        time.sleep(selenium_session.wait_time)
        accept_coockie(selenium_session)
        time.sleep(selenium_session.wait_time)
        save_coockie(selenium_session)
        cookies = selenium_session.driver.get_cookies()
        pickle.dump( selenium_session.driver.get_cookies() , open("cookies.pkl","wb"))
        print("Connection done well")
        return selenium_session