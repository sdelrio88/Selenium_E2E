import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")

    if browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")
