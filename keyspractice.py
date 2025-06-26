
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the key presses practice page
driver.get("https://practice.expandtesting.com/key-presses")

# Locate the input field for key presses
input = driver.find_element(By.ID, "target")

# Send individual key presses to the input field with pauses
input.send_keys(Keys.ADD)
time.sleep(1)
input.send_keys(Keys.SUBTRACT)
time.sleep(1)
input.send_keys(Keys.MULTIPLY)
time.sleep(1)
input.send_keys(Keys.DIVIDE)
time.sleep(1)
input.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
input.send_keys(Keys.ARROW_LEFT)
time.sleep(1)
input.send_keys(Keys.ARROW_RIGHT)
time.sleep(1)
input.send_keys(Keys.ARROW_UP)
time.sleep(1)
input.send_keys(Keys.BACK_SPACE)
time.sleep(1)
input.send_keys(Keys.DELETE)
time.sleep(1)
input.send_keys(Keys.SHIFT)
time.sleep(1)
input.send_keys(Keys.ALT)
time.sleep(1)
input.send_keys(Keys.TAB)
time.sleep(1)
input.send_keys(Keys.CONTROL)
time.sleep(1)
input.send_keys(Keys.HOME)
time.sleep(1)
input.send_keys(Keys.PAGE_UP)
time.sleep(1)
input.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
input.send_keys(Keys.ESCAPE)
time.sleep(1)
input.send_keys(Keys.INSERT)
time.sleep(1)
input.send_keys(Keys.EQUALS)
time.sleep(1)
input.send_keys(Keys.DECIMAL)
time.sleep(1)
input.send_keys(Keys.SEPARATOR)
time.sleep(1)
input.send_keys(Keys.SPACE)
time.sleep(1)
input.send_keys(Keys.EQUALS)
time.sleep(1)

# Create an ActionChains object for keyboard shortcuts
actions = ActionChains(driver)

# Select all text in the input field (Ctrl+A)
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# Copy selected text (Ctrl+C)
actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

time.sleep(1)

# Press Enter in the input field
input.send_keys(Keys.ENTER)

time.sleep(2)

