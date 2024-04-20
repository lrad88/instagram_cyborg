# pip3 install selenium
# knowledge of XPATHs and finding class names in inspect element essential
from selenium import webdriver
from time import sleep
from secrets import details
import random

from selenium.webdriver.common.by import By
from selenium.common.exceptions import (ElementNotInteractableException,
                                        NoSuchElementException)

#chrome_extension_file = File.join(File.dirname(__FILE__), "..",
#        "extension", "testwise-recorder-0.5.2.crx")

#from selenium.webdriver.chrome.service import Service
# selenium web driver allows you to control the browser through txt
# cues

sleep_time = random.uniform(5, 10)

#chromeOptions = Options()
#chromeOptions.headless = True

#driver = webdriver.Chrome()  #options=chromeOptions)


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        # above saves a reference to the username in case it is needed in
        # other methods
        self.driver.get('https://instagram.com/')

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
        sleep(sleep_time)

        #looper = 1

        #while looper != 5:
        #try:

        # Not Now 1
        try:
            self.driver.find_element(By.CLASS_NAME, "_ac8f").click()
            print("1st element found")
            sleep(sleep_time)
        except ElementNotInteractableException:
            print("1st element not found")
            sleep(sleep_time)
        # Not Now 2
        try:

            self.driver.find_element(By.CLASS_NAME,
                                     "_a9-- _ap36 _a9_1").click()
            print("2nd element found")
            sleep(sleep_time)
        except NoSuchElementException:
            print("2nd element not found")
            sleep(sleep_time)
        # Not Now 2 2nd attempt
        try:
            self.driver.find_element(By.XPATH,
                                     "//*[contains(text(), 'Not Now')]").click()
            print("2nd attempt succeeded")
            sleep(sleep_time)
        except ElementNotInteractableException:
            print("2nd attempt failed")
            sleep(sleep_time)
        # New Post
        #try:
        #    self.driver.find_element(By.XPATH, "//aria-label='New post'").click()
        #    print("3rd element found")
        #    sleep(1000)
        #except NoSuchElementException:
        #    print("3rd element not found")
        #    sleep(1000)
        # New Post 2nd attempt (static dropdown menu maybe ?)
        try:
            self.driver.find_element(By.XPATH,
                                     "//*[contains(text(), '#')]").click()
            print("2nd attempt succeeded")
            sleep(1000)
        except ElementNotInteractableException:
            print("2nd attempt failed")
            sleep(1000)

            # Check if the element is visible
            #if element.is_displayed():
            #    looper = 0
            #    print("Element is visible on the page")
            #element = self.driver.find_element(By.XPATH, "//*[contains(text(), 'now')]")
            # above xpath checks all text "*" containing "now"

            #else:
            #    print("Element is not visible on the page")
            #    looper = 1
            #    try:
            #        self.driver.find_element(By.CLASS_NAME,"_ac8f").click()
            #        if element.is_not("_ac8f"):


tha_bot = InstaBot(details()[0], details()[1])
