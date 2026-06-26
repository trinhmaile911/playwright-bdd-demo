from pytest_bdd import given, when, then
from utils.date_helper import parse_date
from steps.common_steps import *


@given("I am on the personal details page")
def open_personal_details_page(personal_details_page):
    personal_details_page.navigate_to_personal_details_page()

@when("I fill data in the First Name textbox")
def input_first_name(personal_details_page, personal_details_data):
    personal_details_page.input_first_name(personal_details_data["valid_user"]["first_name"])

@when("I fill data in the Middle Name textbox")
def input_middle_name(personal_details_page, personal_details_data):
    personal_details_page.input_middle_name(personal_details_data["valid_user"]["middle_name"])

@when("I fill data in the Last Name textbox")
def input_last_name(personal_details_page, personal_details_data):
    personal_details_page.input_last_name(personal_details_data["valid_user"]["last_name"])

@when("I select license expiry date")
def select_license_expiry_date(personal_details_page, personal_details_data):
    license_expiry_date = parse_date(personal_details_data["valid_user"]["license_expiry_date"])
    personal_details_page.select_license_expiry_date(license_expiry_date)

@when("I select gender")
def select_gender(personal_details_page, personal_details_data):
    gender = personal_details_data["valid_user"]["gender"]
    personal_details_page.select_gender(gender)

@when("I click Add button")
def click_add_button(personal_details_page):
    personal_details_page.click_add_button()

@when("I add an attachment")
def add_attachment(personal_details_page, personal_details_data):
    file_path = personal_details_data["valid_user"]["attachment_file_path"]
    personal_details_page.input_attachment(file_path)

@when("I save the attachment uploaded")
def save_attachment(personal_details_page):
    personal_details_page.click_save_file_button()