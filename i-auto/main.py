
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import os
import random
from bs4 import BeautifulSoup as soup 
from urllib.request import Request, urlopen


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options, executable_path='F:\\driver\\chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
URL = "https://www.instagram.com/"


# set facebook user name
usename = "*****"


# set facebook password
password = "*****"


hash = ['message 1', 'message 2']


def login_facebook():
    driver.get(URL)
    sleep(random.randint(1, 4))
    driver.find_element(By.XPATH, "//*/div/div[1]/div/label/input").send_keys(usename)
    sleep(random.randint(1, 4))
    driver.find_element(By.XPATH, "//*/div/div[2]/div/label/input").send_keys(password)
    sleep(random.randint(2, 4))
    driver.find_element(By.XPATH,"//*/div/div[3]/button").submit()
    sleep(random.randint(5, 10))
    print('logged in')


def insta():
    while True:
        driver.get(URL)
        post_msg = random.choice(hash)
        image = "J:\ps\d\wsc\images\1.jpg"
        upload="J:\\ps\\d\\wsc\\images\\"+str(random.randint(1, 10))+".jpg"
        sleep(random.randint(5, 10))
        driver.find_element(By.XPATH, "//*/div/div/div[3]/div/div[3]/div/button/div").click()
        print('add photo clicked')
        sleep(random.randint(5, 10))
        driver.find_element(By.XPATH, "//*/div[2]/div/div/div/div[2]/div[1]/form/input").send_keys(upload)   
        sleep(random.randint(7, 10))
        driver.find_element(By.XPATH, "//*[text()='Next']").click()
        sleep(random.randint(5, 10))
        driver.find_element(By.XPATH, "//*[text()='Next']").click()
        sleep(random.randint(5, 10))
        driver.find_element(By.XPATH, "//*/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea").click()
        actions = ActionChains(driver)  
        actions.send_keys(post_msg)
        actions.perform()
        sleep(random.randint(15, 20))
        sleep(random.randint(5, 10))
        driver.find_element(By.XPATH, "//*/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/label/input").click()
        sleep(random.randint(5, 10))
        actions = ActionChains(driver)  
        actions.send_keys('sarjah')
        actions.perform()
        sleep(random.randint(7, 10))
        button = driver.find_element(By.XPATH, "//button[text()='Share']")
        driver.execute_script("arguments[0].click();", button)
        sleep(random.randint(10, 20))


login_facebook()
insta()
driver.close()
