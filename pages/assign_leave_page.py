from pages.common.date_picker import DatePicker
from utils.date_helper import get_future_date

class AssignLeavePage:
    ASSIGN_LEAVE_URL = "/web/index.php/leave/assignLeave"

    DATE_ICON = '.oxd-date-input-icon'

    def __init__(self, page):
        self.page = page
        self.date_picker = DatePicker(self.page)
        self.from_date_input = self.page.locator(self.DATE_ICON).nth(0)
        self.to_date_input = self.page.locator(self.DATE_ICON).nth(1)

    def navigate_to_assign_leave(self):
        self.page.goto(self.ASSIGN_LEAVE_URL)

    def select_start_date(self, days):
        target = get_future_date(days)
        self.from_date_input.click()
        self.date_picker.select_date(target)

    def select_end_date(self, days):
        target = get_future_date(days)
        self.to_date_input.click()
        self.date_picker.select_date(target)

