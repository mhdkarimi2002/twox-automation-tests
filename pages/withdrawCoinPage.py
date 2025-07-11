from playwright.sync_api import Page

class WithdrawCoinPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.coin = page.get_by_role("button", name="تتر USDT")
        self.addr = page.get_by_role("textbox", name="آدرس")
        self.chain = page.get_by_role("button", name="انتخاب شبکه")
        self.amount = page.get_by_role("textbox", name="مقدار مورد نظر")
        self.next = page.get_by_role("button", name="مرحله بعد")
        self.sendOtp = page.get_by_role("button", name="ارسال پیامک")
        self.otpCode = page.get_by_role("textbox", name="کد تایید")
        self.submit = page.get_by_role("button", name="ثبت و انتقال")

    def withdrawCoin(self):
        self.addr.fill("")
        self.amount.fill("3")
        self.next.click()
        self.sendOtp.click()
        self.otpCode.fill("11111")
        self.submit.click()