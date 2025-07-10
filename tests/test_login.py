from playwright.sync_api import Page, expect
from pages.homePage import HomePage

def test_valid_login(page: Page):
    page.goto("https://dev.twoxdev.ir")

    homePage = HomePage(page)
    result = homePage.login("09035368666", "11111")

    if result == "existing_user":
        expect(homePage.userPanelIcon).to_be_visible()
    elif result == "new_user":
        expect(homePage.registerUser).to_be_visible()
