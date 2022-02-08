import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser n(me e.g. chrome OR firefox")


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome(
            executable_path="/Users/sdelrio/workspace_python/AutomationFramework_1/drivers/chromedriver")
    elif browser == 'firefox':
        driver = webdriver.Firefox(
            executable_path="/Users/sdelrio/workspace_python/AutomationFramework_1/drivers/geckodriver")

    driver.implicitly_wait(5)
    # driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")
