from playwright.sync_api import Page

class HomePage:
    
    def __init__(self, page: Page):
        self.page = page
        self.loginBtn = page.get_by_role("button", name="ورود | ثبت نام")
        self.usernameField = page.get_by_role("textbox", name="شماره موبایل / ایمیل")
        self.sendOtpBtn = page.get_by_role("button", name="ارسال کد")
        self.userPanelIcon = page.get_by_role("img", name="user-panel")
        self.registerUser = page.get_by_role("button", name="بعدا انجام می‌دهم")

    def login(self, username: str, otp: str) -> str:
        self.loginBtn.click()

        self.usernameField.fill(username)
        self.sendOtpBtn.click()

        self.page.wait_for_selector('[id="0"]', timeout=7000)

        for idx, digit in enumerate(otp):
            self.page.locator(f'[id="{idx}"]').fill(digit)

        try:
            self.page.wait_for_selector('img[alt="user-panel"], button:has-text("بعدا انجام می‌دهم")', timeout=8000)
        except:
            raise AssertionError("Login failed: No success UI found (nothing appeared in time).")

        # Determine which appeared
        if self.userPanelIcon.is_visible():
            return "existing_user"
        elif self.registerUser.is_visible():
            return "new_user"
        else:
            raise AssertionError("Login failed: Expected UI was not visible after login.")
