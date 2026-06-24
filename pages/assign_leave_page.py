from pages.common.date_picker import DatePicker
from utils.date_helper import get_future_date
from playwright.sync_api import expect
from re import compile
import time

class AssignLeavePage:
    ASSIGN_LEAVE_URL = "/web/index.php/leave/assignLeave"

    DATE_ICON = ".oxd-date-input-icon"
    EMPLOYEE_NAME_INPUT_PLACEHOLDER = "Type for hints..."
    EMPLOYEE_DROPDOWN_OPTION = ".oxd-autocomplete-option"
    DROPDOWN_ICON = ".oxd-select-text--after"
    COMMENT_INPUT = ".oxd-textarea"
    SUBMIT_BUTTON = "button[type='submit']"
    CONFIRM_DIALOG = ".oxd-sheet"
    CONFIRM_BUTTON_NAME = "Ok"
    TOAST_MESSAGE = ".oxd-toast"

    def __init__(self, page):
        self.page = page
        self.date_picker = DatePicker(self.page)
        self.from_date_input = self.page.locator(self.DATE_ICON).nth(0)
        self.to_date_input = self.page.locator(self.DATE_ICON).nth(1)
        self.employee_name_input = self.page.get_by_placeholder(self.EMPLOYEE_NAME_INPUT_PLACEHOLDER)
        self.dropdown_first_option = self.page.locator(self.EMPLOYEE_DROPDOWN_OPTION).nth(0)
        self.leave_type_icon = self.page.locator(self.DROPDOWN_ICON).nth(0)
        self.dropdown_option = self.page.get_by_role("option")
        self.comment_input = self.page.locator(self.COMMENT_INPUT)
        self.partial_days_icon = self.page.locator(self.DROPDOWN_ICON).nth(1)
        self.duration_icon = self.page.locator(self.DROPDOWN_ICON).nth(2)
        self.toast_message = self.page.locator(self.TOAST_MESSAGE)
        self.submit_button = self.page.locator(self.SUBMIT_BUTTON)
        self.confirm_dialog = self.page.locator(self.CONFIRM_DIALOG)
        self.confirm_button = self.page.get_by_role("button", name=self.CONFIRM_BUTTON_NAME)

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

    def select_first_employee(self, text="a"):
        with self.page.expect_response(lambda r: "/api/v2/pim/employees" in r.url):
            self.employee_name_input.fill(text)
        self.dropdown_first_option.click()

    def select_leave_type(self, leave_type):
        self.leave_type_icon.click()
        self.dropdown_option.filter(has_text=leave_type).click()

    def input_comment(self, text):
        self.comment_input.fill(text)

    def select_partial_days(self, option):
        self.partial_days_icon.click()
        self.dropdown_option.filter(has_text=option).click()

    def select_duration(self, option):
        self.duration_icon.click()
        self.dropdown_option.filter(has_text=option).click()

    def click_submit_button(self):
        self.submit_button.click()

    def click_confirm_button(self):
        self.confirm_button.click()

    def assert_confirm_dialog(self):
        expect(self.confirm_dialog).to_be_visible()

    def assert_toast_message(self):
        expect(self.toast_message).to_be_visible()

