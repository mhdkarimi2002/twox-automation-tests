from playwright.sync_api import Page
from pages.depositCoinPage import DepositCoinPage
from pages.homePage import HomePage

def test_valid_login(page: Page):
    page.goto("https://dev.twoxdev.ir")

    homePage = HomePage(page)
    homePage.login("09035368666", "11111")

    page.goto("https://dev.twoxdev.ir/wallet/deposit/coin")
    depositPage = DepositCoinPage(page)
    addr = depositPage.copyAddr()
    print(addr)