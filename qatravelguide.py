from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://qatravelguide.ccbp.tech/")
time.sleep(1)

# Select Varanasi city
varanasi_button = browser.find_element(By.ID, "varanasi")
varanasi_button.click()
time.sleep(1)

# Switch to details frame
browser.switch_to.frame('frame')

# Print About tab content
about_tab_content = browser.find_element(By.ID, "aboutTabContent")
print(about_tab_content.text)
time.sleep(2)

# Show and print Time to Visit tab content
time_to_visit_button = browser.find_element(By.ID, "timeToVisitButton")
time_to_visit_button.click()
time_to_visit_content = browser.find_element(By.ID, "timeToVisitTabContent")
print(time_to_visit_content.text)
time.sleep(2)

# Show and print Attractions tab content
attractions_button = browser.find_element(By.ID, "attractionsButton")
attractions_button.click()
attractions_content = browser.find_element(By.ID, "attractionsTabContent")
print(attractions_content.text)
time.sleep(2)
