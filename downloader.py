

from selenium import webdriver
from time import sleep

from secrets import details
import random

from selenium.webdriver.common.by import By
from selenium.common.exceptions import (ElementNotInteractableException,
                                        NoSuchElementException, InvalidSelectorException, InvalidArgumentException, ElementClickInterceptedException)
from selenium.webdriver.common.keys import Keys

import pyautogui

sleep_time = random.uniform(2, 3)

class InstaDL:

    def __init__(self, username, password, path, caption):
        self.driver = webdriver.Chrome()
        self.username = username
        # above saves a reference to the username in case it is needed in
        # other methods
        self.driver.get('https://instagram.com/')

        sleep(sleep_time)

# allow all cookies

        try:
            button_element =self.driver.find_element(By.XPATH,"//button[text()='Allow all cookies']")
            button_element.click()
            print("Allow all cookies found")
            sleep(sleep_time)
        except ElementNotInteractableException:
            print("Allow all cookies not found")
            sleep(sleep_time)

# login

        #    .click()
        sleep(sleep_time)
        self.driver.find_element(By.XPATH, "//input[@name=\"username\"]") \
            .send_keys(username)
        # inputs username
        self.driver.find_element(By.XPATH, "//input[@name=\"password\"]") \
            .send_keys(password)
        # inputs password
        self.driver.find_element(By.XPATH, "//button[@type=\"submit\"]") \
            .click()
        # clicks the login button using xpath
        sleep(10)


# save your log in info ? Not Now
        try:
            self.driver.find_element(By.CLASS_NAME, "_ac8f").click()
            print("save your login info found")
            sleep(sleep_time)
        except ElementNotInteractableException:
            print("save your login info not found")
            sleep(sleep_time)

# turn on notifications ? not now
        try:
            self.driver.find_element(By.XPATH,
                                     "//*[contains(text(), 'Not Now')]").click()
            print("Turn on notifications found")
            sleep(sleep_time)
        except ElementNotInteractableException:
            print("Turn on notifications not found")
            sleep(sleep_time)

# press the "more" tab

        try:
            self.driver.find_element(By.XPATH, "//div[contains(@class,'xl5mz7h xhuyl8g')]").click()
            print("more tab found")
            sleep(sleep_time)
        except ElementNotInteractableException:
            print("more tab not found")
            sleep(sleep_time)

# press the "saved" button

        try:
            self.driver.find_element(By.XPATH, "//div[contains(@class,'x9f619 x1n2onr6 x1ja2u2z xdt5ytf x2lah0s x193iq5w xeuugli xamitd3 x78zum5')]").click()
            print("saved button found")
            sleep(sleep_time)
        except (InvalidSelectorException, NoSuchElementException, InvalidArgumentException, ElementClickInterceptedException, ElementNotInteractableException):
            print("saved button not found")
            sleep(sleep_time)

        # press the "saved" button

        try:
            self.driver.find_element(By.XPATH, "//div[contains(@class,'x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _aa-z _ap3g _a6hd')]").click()
            print("saved tab found")
            sleep(1000)
        except (InvalidSelectorException, NoSuchElementException,
                InvalidArgumentException, ElementClickInterceptedException,
                ElementNotInteractableException):
            print("saved tab not found")
            sleep(1000)


ta_bot = InstaDL(details()[0], details()[1], details()[2], details()[3])