from datetime import datetime


class BasePage:
    def __init__(self,page):
        self.page = page

    def goto(self, url:str):
        self.page.goto(url)

    def click(self,locator:str):
        self.page.locator(locator).click()

    def fill_text(self,locator:str,value:str):
        self.page.locator(locator).fill(value)

    def get_text(self,locator:str):
        self.page.locator(locator).inner_text()

    def is_visible(self,locator:str):
        self.page.locator(locator).is_visible()

    def take_screenshot(self,name:str="screenshot.png"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        self.page.screenshot(path=filename)

    def wait_for_element(self,locator:str, timeout:int = 5000):
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)
