from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from Instafollower import *

chrome_driver_path = "C:/Users../chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

INSTAGRAM_URL = "https://www.instagram.com/accounts/login/"
SIMILAR_ACCOUNT_URL = "chefsteps"
USERNAME = "YOURUSER"
PASSWORD = "YOURPASS"


#STEP1) LOGIN TO INSTAGRAM
driver.get(INSTAGRAM_URL)
sleep(2)

close_popup = driver.find_element_by_css_selector('.aOOlW.bIiDR')
close_popup.click()

sleep(2)
driver.find_element_by_name("username").send_keys(USERNAME)
password=driver.find_element_by_name("password").send_keys(PASSWORD,Keys.ENTER)



#STEP2)finding followers and following them

sleep(3)
driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT_URL}/")

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()