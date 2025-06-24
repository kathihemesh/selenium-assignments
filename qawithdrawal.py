from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://qawithdrawal.ccbp.tech/")

# Check username
username_label = browser.find_element(By.CLASS_NAME, "name")
if username_label.text == "Sarah Williams":
    print("Username is correct")
else:
    print("Username is incorrect")

# Check initial balance
balance_label = browser.find_element(By.CSS_SELECTOR, ".balance")
if balance_label.text == "2000":
    print("Initial balance is correct")
else:
    print("Incorrect initial balance")

# Find withdrawal denomination buttons
denomination_buttons = browser.find_elements(By.CSS_SELECTOR, ".denomination-button")
expected_balances = ["1900", "1700", "1300", "300"]

# Test withdrawal for each denomination
for i in range(4):
    denomination_buttons[i].click()
    time.sleep(1)
    denomination_buttons[i].click()
    if balance_label.text == expected_balances[i]:
        print("Withdrawal App working as expected")
    else:
        print("Mismatch found in balance")

time.sleep(5)



