
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options, executable_path='F:\\driver\\chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
URL = "https://www.facebook.com/"

# set facebook user name
fb_usename = "***"

# set facebook password
fb_password = "****"




def login_facebook():
    driver.get(URL)
    driver.find_element_by_id('email').send_keys(fb_usename)
    driver.find_element_by_id('pass').send_keys(fb_password)
    driver.find_element_by_xpath("//button[@name='login']").submit()
    sleep(6)


def group_post():
    # driver.get('https://www.facebook.com/groups/770478273851370')
    post_msg = "text"
    groups_links_list = ['258984621150683', '1753057948265688']
    sleep(5)
    for i in range(len(groups_links_list)):
        link = 'https://www.facebook.com/groups/' + groups_links_list[i]
        driver.get(link)
        sleep(6)
        driver.find_element_by_xpath("//span[contains(text(),'Create a public post…')]").click()
        sleep(3)
        actions = ActionChains(driver)
        actions.send_keys(post_msg)
        actions.perform()
        sleep(5)
        driver.find_element_by_xpath("//*/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div/span/img").click()
        sleep(7)
        driver.find_element_by_xpath("//*/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div/div").click()
        sleep(8)
        driver.find_element_by_xpath("//*/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div").click()
        sleep(8)

login_facebook()
group_post()
driver.close()
