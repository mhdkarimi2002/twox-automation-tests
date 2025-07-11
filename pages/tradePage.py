import re
from playwright.sync_api import Page

class TradePage:
    
    def __init__(self, page: Page):
        self.page = page
        self.firstField = page.locator("div", has_text=re.compile(r"تبدیل ازموجودی")).get_by_role("textbox").nth(0)
        self.secondField = page.locator("div", has_text=re.compile(r"تبدیل بهUSDT")).get_by_role("textbox").nth(1)
        self.buyUSDT = page.get_by_role("button", name="خرید تتر")
        self.confirmBtn = page.get_by_role("button", name="تایید معامله")

    def buy(self, amount: str):
        self.firstField.clear()
        self.firstField.fill(amount)
        self.buyUSDT.click()
        self.page.wait_for_selector("button:has-text('تایید معامله')")  # Ensures button appears before next click
        self.confirmBtn.click()

