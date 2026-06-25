import re
from datetime import datetime
from utils.date_helper import MONTH_NAMES

class DatePicker:
    MONTH_DROPDOWN = '.oxd-calendar-selector-month-selected'
    YEAR_DROPDOWN = '.oxd-calendar-selector-year-selected'
    DROPDOWN_OPTION = '.oxd-calendar-dropdown--option'
    CALENDAR_DATE = '.oxd-calendar-date'

    def __init__(self, page):
        self.page = page
        self.month_dropdown = self.page.locator(self.MONTH_DROPDOWN).first
        self.year_dropdown = self.page.locator(self.YEAR_DROPDOWN).first
        self.calendar_date = self.page.locator(self.CALENDAR_DATE)
        self.dropdown_option = self.page.locator(self.DROPDOWN_OPTION)

    def select_month(self, month_name: str):
        self.month_dropdown.click()
        self.dropdown_option.filter(has_text=month_name).click()

    def select_year(self, year: str):
        self.year_dropdown.click()
        self.dropdown_option.filter(has_text=year).click()

    def click_day(self, day: str):
        self.calendar_date.filter(has_text=re.compile(f"^{day}$")).click()

    def select_date(self, target: datetime):
        self.select_month(MONTH_NAMES[target.month - 1])
        self.select_year(str(target.year))
        self.click_day(str(target.day))
