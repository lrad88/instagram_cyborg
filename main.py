# pip3 install selenium
# knowledge of XPATHs and finding class names in inspect element essential

from selenium import webdriver
from time import sleep

from secrets import details
import random

from selenium.webdriver.common.by import By
from selenium.common.exceptions import (ElementNotInteractableException,
                                        NoSuchElementException)
from selenium.webdriver.common.keys import Keys

import pyautogui

sleep_time = random.uniform(2, 3)


class InstaBot:
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

# open new post tab


        try:
            button_element = self.driver.find_element(By.CSS_SELECTOR,"[aria-label='New post']")
            button_element.click()
            print("open new post tab found")
            sleep(sleep_time)
        except ElementNotInteractableException:
            print("open new post tab not found")
            sleep(sleep_time)

# open post selector box

        try:
            button_element = self.driver.find_element(By.CSS_SELECTOR,"[aria-label='Post']")
            button_element.click()
            print("post selector box found")
            sleep(sleep_time)
        except ElementNotInteractableException:
            print("post selector box not found")
            sleep(sleep_time)

# open file

        try:
            button_element =self.driver.find_element(By.XPATH,"//button[text()='Select From Computer']")
            button_element.click()
            print("File select box found")
            sleep(sleep_time)

            pyautogui.press("/")
            pyautogui.typewrite(path)

            sleep(sleep_time)

            pyautogui.press("enter")

            sleep(sleep_time)

            pyautogui.press("enter")

            print("File selected")
            sleep(20)
        except ElementNotInteractableException:
            print("File select box not found")
            sleep(sleep_time)

# video posts are now shared as reels

        try:
            button_element =self.driver.find_element(By.XPATH,"//button[text()='OK']")
            button_element.click()
            print("Shared as reels button found")
            sleep(sleep_time)
        except ElementNotInteractableException:
            print("Shared as reels button not found")
            sleep(sleep_time)

# cropping settings

        try:
            self.driver.find_element(By.XPATH, "//div[contains(@class,'_ac7b _ac7d')]").click()
            print("cropping settings click through found")
            sleep(sleep_time)
        except ElementNotInteractableException:
            print("cropping settings click through not found")
            sleep(sleep_time)

# editing settings

        try:
            self.driver.find_element(By.XPATH, "//div[contains(@class,'_ac7b _ac7d')]").click()
            print("editing settings click through found")
            sleep(sleep_time)
        except ElementNotInteractableException:
            print("editing settings click through not found")
            sleep(sleep_time)

# write a caption

        try:
            button_element = self.driver.find_element(By.CSS_SELECTOR,"[aria-label='Write a caption...']")
            button_element.click()
            print("Write a caption box found")

            pyautogui.typewrite(caption)

            sleep(1000)

        except ElementNotInteractableException:
            print("Write a caption box not found")
            sleep(sleep_time)

# share

        try:
            self.driver.find_element(By.XPATH,
                                     "//div[contains(@class,'_ac7b _ac7d')]").click()
            print("post successfully shared!")
            sleep(30)
        except ElementNotInteractableException:
            print("Share button not found")
            sleep(sleep_time)







tha_bot = InstaBot(details()[0], details()[1], details()[2], details()[3])
