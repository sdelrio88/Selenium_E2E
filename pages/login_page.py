class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = self.driver.find_element('name', 'username')
        self.password_textbox_id = self.driver.find_element('name', 'password')
        self.login_button_id = self.driver.find_element('css selector', '.orangehrm-login-button')

    def enter_username(self, username):
        self.username_textbox_id.clear()
        self.username_textbox_id.send_keys(username)

    def enter_password(self, password):
        self.password_textbox_id.clear()
        self.password_textbox_id.send_keys(password)

    def click_login(self):
        self.login_button_id.click()