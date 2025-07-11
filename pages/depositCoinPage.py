from playwright.sync_api import Page

class DepositCoinPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.coin = page.locator(".PrivateSwitchBase-input").first.check()
        self.chainDropDown = page.get_by_text("شبکه مورد نظر را انتخاب کنید")
        self.chain = page.locator("div").filter(has_text="انتخاب شبکهETHEthereumTRXTronBSCBNB Smart ChainGTEVMGateChainKAVAEVMKAVA").nth(1)
        self.address = page.get_by_role("img", name="کپی").first

    def copyAddr(self):
        self.chainDropDown.click()
        self.chain.click()
        self.address.click()