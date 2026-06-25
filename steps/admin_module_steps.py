import time
from pytest_bdd import given, when, then, parsers

@given("I am on the dashboard page")
def open_dashboard_page(dashboard_page):
    dashboard_page.navigate_to_dashboard()

@when("I open the Admin module")
def open_admin_module(dashboard_page):
    dashboard_page.open_admin_page()

@when("I click Add user")
def click_add_user(user_management_page):
    user_management_page.click_add_user()

@when("I cancel adding user")
def cancel_add_user(add_user_page):
    add_user_page.click_cancel()

@when(parsers.parse("I select user role {user_role}"))
def select_user_role(add_user_page, user_role):
    add_user_page.select_user_role(user_role)

@when(parsers.parse("I select status {status}"))
def select_status(add_user_page, status):
    add_user_page.select_status(status)

@when(parsers.parse("I enter employee name as {employee_name}"))
def select_employee_name(add_user_page, employee_name):
    add_user_page.select_employee_name(employee_name)

@when(parsers.parse("I enter username {username}"))
def enter_username(add_user_page, scenario_context, username):
    unique_username = f"{username}_{int(time.time())}"
    add_user_page.enter_username(unique_username)
    scenario_context["username"] = unique_username

@when(parsers.parse("I enter password {password}"))
def enter_password(add_user_page, password):
    add_user_page.enter_password(password)

@when(parsers.parse("I confirm password {password}"))
def confirm_password(add_user_page, password):
    add_user_page.confirm_password(password)

@when("I save the data")
def save_data(add_user_page):
    add_user_page.click_save_button()

@then("I should see the Add User page")
def verify_add_user_page(add_user_page):
    add_user_page.expect_add_user_displayed()

@then("I should see the System Users page")
def verify_system_users_page(user_management_page, api_utils, created_system_users, scenario_context):
    user_management_page.expect_system_users_displayed()

    username = scenario_context.get("username")
    if username:
        user_id = api_utils.get_system_user_id_by_username(username)
        created_system_users.append(user_id)
        assert user_id is not None, f"User {username} was not created"