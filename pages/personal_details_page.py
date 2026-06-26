from pages.base_page import BasePage
from pages.common.date_picker import DatePicker

class PersonalDetailsPage(BasePage):
    PERSONAL_DETAILS_URL = "/web/index.php/pim/viewPersonalDetails/empNumber/7"

    FIRST_NAME_INPUT_PLACEHOLDER = "First Name"
    MIDDLE_NAME_INPUT_PLACEHOLDER = "Middle Name"
    LAST_NAME_INPUT_PLACEHOLDER = "Last Name"
    DATE_ICON = ".oxd-date-input-icon"
    GENDER_RADIO = ".oxd-radio-wrapper"
    ADD_FILE_BUTTON_TEXT = "Add"
    FILE_INPUT = "input[type='file']"
    SAVE_BUTTON_TEXT = "Save"

    VALID_GENDERS = ["Male", "Female"]

    def __init__(self, page):
        super().__init__(page)
        self.date_picker = DatePicker(self.page)
        self.first_name_input = self.page.get_by_placeholder(self.FIRST_NAME_INPUT_PLACEHOLDER)
        self.middle_name_input = self.page.get_by_placeholder(self.MIDDLE_NAME_INPUT_PLACEHOLDER)
        self.last_name_input = self.page.get_by_placeholder(self.LAST_NAME_INPUT_PLACEHOLDER)
        self.license_expiry_date_input = self.page.locator(self.DATE_ICON).nth(0)
        self.gender_radio = self.page.locator(self.GENDER_RADIO)
        self.add_file_button = self.page.get_by_role("button", name=self.ADD_FILE_BUTTON_TEXT)
        self.file_input = self.page.locator(self.FILE_INPUT)
        self.save_file_button = self.page.get_by_role("button", name=self.SAVE_BUTTON_TEXT).nth(1)

    def navigate_to_personal_details_page(self):
        self.navigate(self.PERSONAL_DETAILS_URL)

    def input_first_name(self, first_name):
        self.first_name_input.click()
        self.first_name_input.clear()
        self.first_name_input.fill(first_name)

    def input_middle_name(self, middle_name):
        self.middle_name_input.click()
        self.middle_name_input.clear()
        self.middle_name_input.fill(middle_name)

    def input_last_name(self, last_name):
        self.last_name_input.click()
        self.last_name_input.clear()
        self.last_name_input.fill(last_name)

    def select_license_expiry_date(self, date):
        self.license_expiry_date_input.click()
        self.date_picker.select_date(date)

    def select_gender(self, gender):
        if gender not in self.VALID_GENDERS:
            raise ValueError(f"Invalid gender: {gender}")

        self.gender_radio.filter(has_text=gender).click()

    def click_add_button(self):
        self.add_file_button.click()

    def input_attachment(self, file_path):
        self.file_input.set_input_files(file_path)

    def click_save_file_button(self):
        self.save_file_button.click()