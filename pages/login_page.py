from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    url = "https://the-internet.herokuapp.com/login"

    def __init__(self, page: Page):
        super().__init__(page)

        self.username_input = self.page.locator("#username")
        self.password_input = self.page.locator("#password")
        self.submit = self.page.locator("button[type='submit']")

    def goto_url(self):
        super().goto(self.url)

    def login_to_app(self,username,password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit.click()






