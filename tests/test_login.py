import pytest
import allure
import moment
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_user_menu()
            homepage.click_logout()
            title = driver.title
            assert title == "OrangeHRM"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currentTime = moment.now().format("YYYY-M-D")
            testName = utils.whoami()
            screenshotName = testName + "_" + currentTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            raise
