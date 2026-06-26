from pages.base_page import BasePage


class DashboardPage(BasePage):
    DASHBOARD_URL = "/web/index.php/dashboard/index"

    MENU_ITEM = ".oxd-main-menu-item"
    ADMIN_MODULE_TEXT = "Admin"

    def __init__(self, page):
        super().__init__(page)
        self.admin_menu = page.locator(self.MENU_ITEM).filter(has_text=self.ADMIN_MODULE_TEXT)

    def navigate_to_dashboard(self):
        self.navigate(self.DASHBOARD_URL)

    def open_admin_page(self):
        self.admin_menu.click()



