from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver
browser = webdriver.Chrome()
browser.get("https://qapodcastpage.ccbp.tech/")
time.sleep(1)

# Find all podcast items
podcast_cards = browser.find_elements(By.XPATH, "//div[@class='details-card']")

# Iterate through each podcast card
for i in range(4):
    podcast_cards[i].click()
    time.sleep(2)
    # Find all episodes for the selected podcast
    episode_containers = browser.find_elements(By.XPATH, "//div[@class='podcast-episode-container']")
    if len(episode_containers) == 4:
        print("All 4 Episodes Found.")
    else:
        print("Only" + str(len(episode_containers)) + "Episodes Found.")
    # Go back to the main page
    back_button = browser.find_element(By.XPATH, "//button[contains(text(),'Back')]")
    back_button.click()
    time.sleep(2)



