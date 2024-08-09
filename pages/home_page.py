class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.user_menu_dropdown = '.oxd-userdropdown'
        self.logout_button = '//a[text()=\'Logout\']'

    def click_user_menu(self):
        self.driver.find_element('css selector', self.user_menu_dropdown).click()

    def click_logout(self):
        self.driver.find_element('xpath', self.logout_button).click()
