from pages.base_page import BasePage
from playwright.sync_api import expect


class UserManagementPage(BasePage):
    SYSTEM_USERS_TITLE = ".oxd-table-filter-title"

    ADMIN_TEXT = "Admin"
    ADD_BUTTON_TEXT = "Add"
    SYSTEM_USERS_TITLE_TEXT = "System Users"

    def __init__(self, page):
        super().__init__(page)
        self.add_button = page.get_by_role("button", name=self.ADD_BUTTON_TEXT)
        self.system_users_title = page.locator(self.SYSTEM_USERS_TITLE)

    def click_add_user(self):
        self.add_button.click()

    def expect_system_users_displayed(self):
        expect(self.system_users_title).to_have_text(self.SYSTEM_USERS_TITLE_TEXT, timeout=30000)



