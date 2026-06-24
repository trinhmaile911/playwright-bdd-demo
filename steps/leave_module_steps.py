from pytest_bdd import given, when, then, parsers
import time
@given("I am on the assign leave page")
def open_assign_leave_page(assign_leave_page):
    assign_leave_page.navigate_to_assign_leave()

@when(parsers.parse("I select start date as {days} days from now"))
def select_start_date(assign_leave_page, days):
    assign_leave_page.select_start_date(days)

@when(parsers.parse("I select end date as {days} days from now"))
def select_end_date(assign_leave_page, days):
    assign_leave_page.select_end_date(days)

@when("I select an employee name")
def select_employee_name(assign_leave_page):
    assign_leave_page.select_first_employee()

@when(parsers.parse("I select leave type '{leave_type}'"))
def select_leave_type(assign_leave_page, leave_type):
    assign_leave_page.select_leave_type(leave_type)

@when(parsers.parse("I leave a comment '{comment}'"))
def input_comment(assign_leave_page, comment):
    assign_leave_page.input_comment(comment)

@when(parsers.parse("I select Partial days option as '{option}'"))
def select_partial_days(assign_leave_page, option):
    assign_leave_page.select_partial_days(option)

@when(parsers.parse("I select Duration option as '{option}'"))
def select_duration(assign_leave_page, option):
    assign_leave_page.select_duration(option)

@when("I click on the confirm button")
def click_confirm_button(assign_leave_page):
    assign_leave_page.click_confirm_button()

@then("I should see a confirm dialog")
def assert_confirm_dialog(assign_leave_page):
    assign_leave_page.click_submit_button()
    assign_leave_page.assert_confirm_dialog()

@then("I should see a toast message")
def assert_toast_message(assign_leave_page):
    assign_leave_page.assert_toast_message()