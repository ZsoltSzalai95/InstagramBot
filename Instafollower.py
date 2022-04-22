from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException
from random import randint

INSTAGRAM_URL = "https://www.instagram.com/accounts/login/"
SIMILAR_ACCOUNT_URL = "chefsteps"
USERNAME = "YOURUSER"
PASSWORD = "YOURPASS"

CHROME_DRIVER_PATH = "C:/Users/../chromedriver.exe"




class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get(INSTAGRAM_URL)
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT_URL}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('html/body/div[5]/div/div/div[2]')

        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            #Using Python the solution looks as follows:
            #element_inside_popup = self.driver.find_element_by_xpath("your_element")
            #element_inside_popup.send_keys(Keys.END)
            time.sleep(2)

    def follow(self):
        list_buttons = self.find_elements_by_css_selector("li button")
        try:
            for button in list_buttons:
                if button.text == "Follow":
                    button.click()
                    time.sleep(2)

        except ElementClickInterceptedException:
            if button.text == "Cancel":
                button.click()
            else:
                pass




