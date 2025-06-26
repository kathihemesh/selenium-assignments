# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pytest
# import time
# class TestLoginPage:
#     @pytest.fixture
#     def chromedriver():
#         driver=webdriver.Chrome()
#         driver.maximize_window()
#         driver.implicitly_wait(5)
#         yield driver
#         driver.quit()
#     @pytest.mark.emptyinputs
#     def testLoginWithEmptyInputs(chromedriver):
#         chromedriver.get("https://qajobbyapp.ccbp.tech/login")
#         username=chromedriver.find_element(By.ID,"userNameInput")
#         password=chromedriver.find_element(By.ID,"passwordInput")
#         username.send_keys("")
#         password.send_keys("")
#         loginbtn=chromedriver.find_element(By.CLASS_NAME,"login-button")
#         loginbtn.click()
#         error=chromedriver.find_element(By.CLASS_NAME,"error-message")
#         assert error.is_displayed()
#     @pytest.mark.emptyusername
#     def testLoginWithEmptyUsername(chromedriver):
#         chromedriver.get("https://qajobbyapp.ccbp.tech/login")
#         username=chromedriver.find_element(By.ID,"userNameInput")
#         password=chromedriver.find_element(By.ID,"passwordInput")
#         username.send_keys("")
#         password.send_keys("rahul@2021")
#         loginbtn=chromedriver.find_element(By.CLASS_NAME,"login-button")
#         loginbtn.click()
#         error=chromedriver.find_element(By.CLASS_NAME,"error-message")
#         assert error.is_displayed()
#     @pytest.mark.emptypassword
#     def testLoginWithEmptyPassword(chromedriver):
#         chromedriver.get("https://qajobbyapp.ccbp.tech/login")
#         username=chromedriver.find_element(By.ID,"userNameInput")
#         password=chromedriver.find_element(By.ID,"passwordInput")
#         username.send_keys("rahul")
#         password.send_keys("")
#         loginbtn=chromedriver.find_element(By.CLASS_NAME,"login-button")
#         loginbtn.click()
#         error=chromedriver.find_element(By.CLASS_NAME,"error-message")
#         assert error.is_displayed()
#     # @pytest.mark.invalidpassword
#     # def testLoginWithEmptyPassword1(chromedriver):
#     #     chromedriver.get("https://qajobbyapp.ccbp.tech/login")
#     #     username=chromedriver.find_element(By.ID,"userNameInput")
#     #     password=chromedriver.find_element(By.ID,"passwordInput")
#     #     username.send_keys("rahul")
#     #     password.send_keys("abcd")
#     #     loginbtn=chromedriver.find_element(By.CLASS_NAME,"login-button")
#     #     loginbtn.click()
#     #     error=chromedriver.find_element(By.CLASS_NAME,"error-message")
#     #     assert error.text=="*username and password didn't match"
#     @pytest.mark.invalidpassword
#     def testLoginWithInvalidPassword(chromedriver):
#         chromedriver.get("https://qajobbyapp.ccbp.tech/login")
#         username = chromedriver.find_element(By.ID, "userNameInput")
#         password = chromedriver.find_element(By.ID, "passwordInput")
#         username.send_keys("rahul")
#         password.send_keys("abcd")
#         loginbtn = chromedriver.find_element(By.CLASS_NAME, "login-button")
#         loginbtn.click()
#         error = chromedriver.find_element(By.CLASS_NAME, "error-message")
#         assert error.text == "*username and password didn't match"

#     @pytest.mark.successlogin
#     def testLoginWithValidCreds(chromedriver):
#         chromedriver.get("https://qajobbyapp.ccbp.tech/login")
#         username=chromedriver.find_element(By.ID,"userNameInput")
#         password=chromedriver.find_element(By.ID,"passwordInput")
#         username.send_keys("rahul")
#         password.send_keys("rahul@2021")
#         loginbtn=chromedriver.find_element(By.CLASS_NAME,"login-button")
#         loginbtn.click()
#         assert chromedriver.current_url=="https://qajobbyapp.ccbp.tech/"
# class HomePageTest():
#     @pytest.fixture
#     def chromedriver():
#         driver=webdriver.Chrome()
#         driver.maximize_window()
#         driver.implicitly_wait()
#         yield driver
#         driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# ✅ Move the fixture outside the class
@pytest.fixture
def chromedriver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

class TestLoginPage:

    @pytest.mark.emptyinputs
    def testLoginWithEmptyInputs(self, chromedriver):
        chromedriver.get("https://qajobbyapp.ccbp.tech/login")
        chromedriver.find_element(By.ID, "userNameInput").send_keys("")
        chromedriver.find_element(By.ID, "passwordInput").send_keys("")
        chromedriver.find_element(By.CLASS_NAME, "login-button").click()
        error = chromedriver.find_element(By.CLASS_NAME, "error-message")
        assert error.is_displayed()

    @pytest.mark.emptyusername
    def testLoginWithEmptyUsername(self, chromedriver):
        chromedriver.get("https://qajobbyapp.ccbp.tech/login")
        chromedriver.find_element(By.ID, "userNameInput").send_keys("")
        chromedriver.find_element(By.ID, "passwordInput").send_keys("rahul@2021")
        chromedriver.find_element(By.CLASS_NAME, "login-button").click()
        error = chromedriver.find_element(By.CLASS_NAME, "error-message")
        assert error.is_displayed()

    @pytest.mark.emptypassword
    def testLoginWithEmptyPassword(self, chromedriver):
        chromedriver.get("https://qajobbyapp.ccbp.tech/login")
        chromedriver.find_element(By.ID, "userNameInput").send_keys("rahul")
        chromedriver.find_element(By.ID, "passwordInput").send_keys("")
        chromedriver.find_element(By.CLASS_NAME, "login-button").click()
        error = chromedriver.find_element(By.CLASS_NAME, "error-message")
        assert error.is_displayed()

    @pytest.mark.invalidpassword
    def testLoginWithInvalidPassword(self, chromedriver):
        chromedriver.get("https://qajobbyapp.ccbp.tech/login")
        chromedriver.find_element(By.ID, "userNameInput").send_keys("rahul")
        chromedriver.find_element(By.ID, "passwordInput").send_keys("abcd")
        chromedriver.find_element(By.CLASS_NAME, "login-button").click()
        error = chromedriver.find_element(By.CLASS_NAME, "error-message")
        assert error.text == "*username and password didn't match"

    @pytest.mark.successlogin
    def testLoginWithValidCreds(self, chromedriver):
        chromedriver.get("https://qajobbyapp.ccbp.tech/login")
        chromedriver.find_element(By.ID, "userNameInput").send_keys("rahul")
        chromedriver.find_element(By.ID, "passwordInput").send_keys("rahul@2021")
        chromedriver.find_element(By.CLASS_NAME, "login-button").click()
        assert chromedriver.current_url == "https://qajobbyapp.ccbp.tech/"
