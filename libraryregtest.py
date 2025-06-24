from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Initialize the Chrome WebDriver
browser = webdriver.Chrome()
browser.get("https://libraryregtest.ccbp.tech/")

# Locate form fields
full_name_input = browser.find_element(By.NAME, "fullName")
male_radio = browser.find_element(By.ID, "male")
contact_number_input = browser.find_element(By.ID, "contactNumber")
email_input = browser.find_element(By.ID, "email")
membership_dropdown = browser.find_element(By.ID, "membershipType")
membership_selector = Select(membership_dropdown)
fiction_checkbox = browser.find_element(By.ID, "fiction")
science_checkbox = browser.find_element(By.ID, "science")
agreement_checkbox = browser.find_element(By.ID, "agreement")
submit_button = browser.find_element(By.CLASS_NAME, "submit-btn")

# Fill out the form
full_name_input.send_keys("Kathi Hemesh Reddy")
time.sleep(1)
male_radio.click()
time.sleep(1)
contact_number_input.send_keys("999999999")
time.sleep(1)
email_input.send_keys("hemesh@gmail.com")
time.sleep(1)
membership_selector.select_by_value("individual")
time.sleep(1)
fiction_checkbox.click()
time.sleep(1)
science_checkbox.click()
time.sleep(1)
agreement_checkbox.click()
time.sleep(1)
submit_button.click()
time.sleep(3)