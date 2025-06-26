from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome and open the upload page
browser = webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com/upload")

file_input = browser.find_element(By.ID, "file-upload")
file_path = "C:\\Screenshot 2025-03-25 115943.png"  # Update this path as needed
file_input.send_keys(file_path)

upload_button = browser.find_element(By.ID, "file-submit")
time.sleep(2)
upload_button.click()

print("Upload successful")
time.sleep(3)
# browser.quit()  # Uncomment to close the browser after upload
