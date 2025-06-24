from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome WebDriver
browser = webdriver.Chrome()
browser.get("https://qaflightbooking.ccbp.tech/")

# Locate input fields
departure_city_input = browser.find_element(By.ID, "departureCity")
destination_city_input = browser.find_element(By.ID, "destinationCity")
travel_date_input = browser.find_element(By.ID, "travelDate")
passengers_input = browser.find_element(By.ID, "passengers")

# Fill in flight details
departure_city_input.send_keys("New York")
time.sleep(1)
destination_city_input.send_keys("Los Angeles")
time.sleep(1)
travel_date_input.send_keys("01/08/2023")
time.sleep(1)
passengers_input.send_keys("2")
time.sleep(1)

# Wait for and click search button
wait = WebDriverWait(browser, 5)
search_button = wait.until(EC.element_to_be_clickable((By.ID, "searchBtn")))
search_button.click()
time.sleep(1)

# Select flight and book
flight_radio = browser.find_element(By.CSS_SELECTOR, "input[value='0']")
flight_radio.click()
time.sleep(2)
book_now_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Book Now']")))
book_now_button.click()

# Print wallet balance
wallet_balance_text = browser.find_element(By.XPATH, "//p[contains(text(),'Your wallet')]")
print(wallet_balance_text.text)

# Enter password and pay
password_input = browser.find_element(By.CSS_SELECTOR, "input[type='password']")
password_input.send_keys("traveler123")
pay_now_button = browser.find_element(By.XPATH, "//button[text()='Pay Now']")
time.sleep(2)
pay_now_button.click()

# Wait for and print booking success message
success_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Booking Success!']")))
print(success_message.text)
time.sleep(3)
