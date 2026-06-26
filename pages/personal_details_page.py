from pages.common.date_picker import DatePicker

class PersonalDetailsPage:
    PERSONAL_DETAILS_URL = "/web/index.php/pim/viewPersonalDetails/empNumber/7"

    FIRST_NAME_INPUT_PLACEHOLDER = "First Name"
    MIDDLE_NAME_INPUT_PLACEHOLDER = "Middle Name"
    LAST_NAME_INPUT_PLACEHOLDER = "Last Name"
    DATE_ICON = ".oxd-date-input-icon"
    GENDER_RADIO = ".oxd-radio-wrapper"
    VALID_GENDERS = ["Male", "Female"]

    def __init__(self, page):
        self.page = page
        self.date_picker = DatePicker(self.page)
        self.first_name_input = self.page.get_by_placeholder(self.FIRST_NAME_INPUT_PLACEHOLDER)
        self.middle_name_input = self.page.get_by_placeholder(self.MIDDLE_NAME_INPUT_PLACEHOLDER)
        self.last_name_input = self.page.get_by_placeholder(self.LAST_NAME_INPUT_PLACEHOLDER)
        self.license_expiry_date_input = self.page.locator(self.DATE_ICON).nth(0)
        self.gender_radio = self.page.locator(self.GENDER_RADIO)

    def navigate_to_personal_details_page(self):
        self.page.goto(self.PERSONAL_DETAILS_URL)

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
