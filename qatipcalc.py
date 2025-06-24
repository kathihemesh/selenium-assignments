from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver
browser = webdriver.Chrome()
browser.get("https://qatipcalc.ccbp.tech/")

# Locate input fields
bill_amount_input = browser.find_element(By.CSS_SELECTOR, "#billAmount")
bill_amount_input.send_keys("1000")
time.sleep(1)
percentage_input = browser.find_element(By.CSS_SELECTOR, "#percentageTip")
percentage_input.send_keys("12")
time.sleep(2)

# Calculate tip
calculate_button = browser.find_element(By.CSS_SELECTOR, "#calculateButton")
calculate_button.click()
tip_amount_text = browser.find_element(By.CSS_SELECTOR, "#tipAmount")
total_amount_text = browser.find_element(By.CSS_SELECTOR, "#totalAmount")
time.sleep(1)

# Check tip and total amount
if tip_amount_text.text == "120.00" and total_amount_text.text == "1120.00":
    print("Tip Calculated Correctly")
else:
    print("Tip Calculated Incorrectly")

# Test error for empty percentage
percentage_input.clear()
time.sleep(1)
calculate_button.click()
time.sleep(2)
error_message = browser.find_element(By.CSS_SELECTOR, "#errorMessage")
if error_message.text == "Please Enter a Valid Input.":
    print("Error message displayed for no input")
else:
    print("Error message missing for no input")

# Test error for invalid percentage
percentage_input.send_keys("10f")
time.sleep(1)
calculate_button.click()
if error_message.text == "Please Enter a Valid Input.":
    print("Error message displayed for invalid input")
else:
    print("Error message missing for invalid input")
time.sleep(1)
