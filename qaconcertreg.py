from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver
browser = webdriver.Chrome()
browser.get("https://qaconcertreg.ccbp.tech/")

# Locate form fields and buttons
name_input = browser.find_element(By.ID, "name")
email_input = browser.find_element(By.ID, "email")
book_now_button = browser.find_element(By.CSS_SELECTOR, ".btn")

# Enter name and try to book
name_input.send_keys("Charlie")
time.sleep(1)
book_now_button.click()
alert = browser.switch_to.alert
print(alert.text)
time.sleep(1)
alert.accept()

# Enter email and try to book
email_input.send_keys("charlie@example.com")
time.sleep(1)
book_now_button.click()
print(alert.text)
time.sleep(1)
alert.accept()
time.sleep(1)

# Enter passcode and verify
passcode_input = browser.find_element(By.ID, "passcode")
passcode_input.send_keys("123456")
time.sleep(1)
verify_button = browser.find_element(By.XPATH, "//button[text()='Verify']")
verify_button.click()
time.sleep(1)
print(alert.text)
alert.accept()
print(alert.text)
time.sleep(1)
alert.accept()
time.sleep(1)

# Enter gift voucher code
alert.send_keys("foodmunch")
time.sleep(1)
alert.accept()
time.sleep(1)
print("Gift Voucher Issued")

