
import pytest
import allure
import moment
from pages.loginPage import LoginPage
from pages.homePage import HomePage
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
            homepage.click_welcome()
            homepage.click_logout()
            title = driver.title
            assert title == "abc"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currentTime = moment.now().format("MMMM D YYYY, h:mm:ss a")
            testName = utils.whoami()
            screenshotName = testName + "_" + currentTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            
            #store screenshot physically
            driver.get_screenshot_as_file("/Users/sdelrio/workspace_python/AutomationFramework_1/screenshots/" + screenshotName + ".png")
            raise

        except:
            print("There was an exception")
            currentTime = moment.now().format("MMMM D YYYY, h:mm:ss a")
            testName = utils.whoami()
            screenshotName = testName + "_" + currentTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            raise

        else:
            print("No exceptions occurred")

        finally:
            print("I am inside finally block")
