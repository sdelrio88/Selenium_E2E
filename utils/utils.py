#CONSTANTS

#NOTES
# For running tests on command line: python -m pytest
# For running tests with html reports: python -m pytest --html=reports/report1.html
# For running tests with html reports: python -m pytest --html=reports/report1.html --self-contained-html

#For running with allure reports: python -m pytest --alluredir=reports/allure-reports
#Generate the reports for viewing : allure serve reports//allure-reportss
import inspect

URL = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "Admin"
PASSWORD = "admin123"

def whoami():
    return inspect.stack()[1][3]
