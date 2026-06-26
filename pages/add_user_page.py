from pages.base_page import BasePage
from playwright.sync_api import expect


class AddUserPage(BasePage):
    ADD_USER_TITLE_SELECTOR = ".orangehrm-main-title"
    DROPDOWN_SELECTOR = ".oxd-select-text"
    DROPDOWN_INPUT_SELECTOR = ".oxd-select-text-input"
    DROPDOWN_PANEL_SELECTOR = ".oxd-select-dropdown"
    INPUT_GROUP = ".oxd-input-group"
    AUTOCOMPLETE_OPTION = ".oxd-autocomplete-option"

    ADD_USER_TITLE_TEXT = "Add User"
    CANCEL_BUTTON_TEXT = "Cancel"
    USERNAME_LABEL = "Username"
    PASSWORD_LABEL = "Password"
    CONFIRM_PASSWORD_LABEL = "Confirm password"
    EMPLOYEE_NAME_PLACEHOLDER = "Type for hints..."
    SAVE_BUTTON_TEXT = "Save"

    def __init__(self, page):
        super().__init__(page)
        self.cancel_button = page.get_by_role("button", name=self.CANCEL_BUTTON_TEXT)
        self.add_user_title = page.locator(self.ADD_USER_TITLE_SELECTOR)
        self.employee_name_input = page.get_by_placeholder(self.EMPLOYEE_NAME_PLACEHOLDER)
        self.username_input = page.locator(self.INPUT_GROUP).filter(
            has_text=self.USERNAME_LABEL
        ).locator("input")
        self.password_input = page.locator(self.INPUT_GROUP).filter(
            has_text=self.PASSWORD_LABEL
        ).locator("input").first
        self.confirm_password_input = page.locator(self.INPUT_GROUP).filter(
            has_text=self.CONFIRM_PASSWORD_LABEL
        ).locator("input")
        self.save_button = page.get_by_role("button", name=self.SAVE_BUTTON_TEXT)

        self.user_role_dropdown = page.locator(self.DROPDOWN_SELECTOR).nth(0)
        self.status_dropdown = page.locator(self.DROPDOWN_SELECTOR).nth(1)

    def click_cancel(self):
        self.cancel_button.click()

    def expect_add_user_displayed(self):
        expect(self.add_user_title).to_have_text(self.ADD_USER_TITLE_TEXT)

    def _select_option(self, dropdown, option_text):
        dropdown.locator(self.DROPDOWN_INPUT_SELECTOR).click()

        dropdown_panel = self.page.locator(self.DROPDOWN_PANEL_SELECTOR)
        dropdown_panel.wait_for(state="visible")

        raw_options = dropdown_panel.locator("div").all_inner_texts()
        clean_options = []

        for raw_option in raw_options:
            cleaned_option = raw_option.strip()

            if cleaned_option:
                clean_options.append(cleaned_option)

        if option_text not in clean_options:
            raise ValueError(
                f'Option "{option_text}" not found. Available options: {clean_options}'
            )

        option_index = clean_options.index(option_text)

        for _ in range(option_index):
            self.page.keyboard.press("ArrowDown")

        self.page.keyboard.press("Enter")

        expect(dropdown).to_contain_text(option_text)

    def select_user_role(self, user_role):
        self._select_option(self.user_role_dropdown, user_role)

    def select_status(self, status):
        self._select_option(self.status_dropdown, status)

    def select_employee_name(self, employee_name):
        self.employee_name_input.fill(employee_name)

        option = self.page.locator(self.AUTOCOMPLETE_OPTION).filter(
            has_text=employee_name
        )

        option.click()

    def enter_username(self, username):
        self.username_input.fill(username)

    def enter_password(self, password):
        self.password_input.fill(password)

    def confirm_password(self, password):
        self.confirm_password_input.fill(password)

    def click_save_button(self):
        self.save_button.click()