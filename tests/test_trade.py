from playwright.sync_api import Page
from pages.tradePage import TradePage
from pages.homePage import HomePage

def test_valid_login(page: Page):
    page.goto("https://dev.twoxdev.ir")

    homePage = HomePage(page)
    homePage.login("09035368666", "11111")

    page.goto("https://dev.twoxdev.ir/trade")

    tradePage = TradePage(page)
    tradePage.buy("350000")