import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Fixture to initialize and quit the Chrome WebDriver for each test
@pytest.fixture
def chromedriver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

class TestLoginPage:
    # Test: Login with both fields empty
    @pytest.mark.emptyinputs
    def testLoginWithEmptyInputs(self, chromedriver):
        chromedriver.get("https://qajobbyapp.ccbp.tech/login")
        chromedriver.find_element(By.ID, "userNameInput").send_keys("")
        chromedriver.find_element(By.ID, "passwordInput").send_keys("")
        chromedriver.find_element(By.CLASS_NAME, "login-button").click()
        error = chromedriver.find_element(By.CLASS_NAME, "error-message")
        assert error.is_displayed()

    # Test: Login with empty username
    @pytest.mark.emptyusername
    def testLoginWithEmptyUsername(self, chromedriver):
        chromedriver.get("https://qajobbyapp.ccbp.tech/login")
        chromedriver.find_element(By.ID, "userNameInput").send_keys("")
        chromedriver.find_element(By.ID, "passwordInput").send_keys("rahul@2021")
        chromedriver.find_element(By.CLASS_NAME, "login-button").click()
        error = chromedriver.find_element(By.CLASS_NAME, "error-message")
        assert error.is_displayed()

    # Test: Login with empty password
    @pytest.mark.emptypassword
    def testLoginWithEmptyPassword(self, chromedriver):
        chromedriver.get("https://qajobbyapp.ccbp.tech/login")
        chromedriver.find_element(By.ID, "userNameInput").send_keys("rahul")
        chromedriver.find_element(By.ID, "passwordInput").send_keys("")
        chromedriver.find_element(By.CLASS_NAME, "login-button").click()
        error = chromedriver.find_element(By.CLASS_NAME, "error-message")
        assert error.is_displayed()

    # Test: Login with invalid password
    @pytest.mark.invalidpassword
    def testLoginWithInvalidPassword(self, chromedriver):
        chromedriver.get("https://qajobbyapp.ccbp.tech/login")
        chromedriver.find_element(By.ID, "userNameInput").send_keys("rahul")
        chromedriver.find_element(By.ID, "passwordInput").send_keys("abcd")
        chromedriver.find_element(By.CLASS_NAME, "login-button").click()
        error = chromedriver.find_element(By.CLASS_NAME, "error-message")
        assert error.text == "*username and password didn't match"

    # Test: Login with valid credentials
    @pytest.mark.successlogin
    def testLoginWithValidCreds(self, chromedriver):
        chromedriver.get("https://qajobbyapp.ccbp.tech/login")
        chromedriver.find_element(By.ID, "userNameInput").send_keys("rahul")
        chromedriver.find_element(By.ID, "passwordInput").send_keys("rahul@2021")
        chromedriver.find_element(By.CLASS_NAME, "login-button").click()
        # Explicit wait for URL to change after successful login
        wait = WebDriverWait(chromedriver, 5)
        wait.until(EC.url_changes("https://qajobbyapp.ccbp.tech/login"))
        time.sleep(1)
        # Assert that the user is redirected to the home page
        assert chromedriver.current_url == "https://qajobbyapp.ccbp.tech/"
