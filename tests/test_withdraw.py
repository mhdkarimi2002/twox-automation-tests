from playwright.sync_api import Page
from pages.withdrawCoinPage import WithdrawCoinPage
from pages.homePage import HomePage

def test_valid_login(page: Page):
    page.goto("https://dev.twoxdev.ir")

    homePage = HomePage(page)
    homePage.login("09035368666", "11111")

    page.goto("https://release.twoxdev.ir/wallet/withdraw/coin")

    withdrawPage = WithdrawCoinPage(page)
    withdrawPage.withdrawCoin()
