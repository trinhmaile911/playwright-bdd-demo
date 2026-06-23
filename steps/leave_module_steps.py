from pytest_bdd import given, when, then, parsers

@given("I am on the assign leave page")
def open_assign_leave_page(assign_leave_page):
    assign_leave_page.navigate_to_assign_leave()

@when(parsers.parse("I select start date as {days} days from now"))
def select_start_date(assign_leave_page, days):
    assign_leave_page.select_start_date(days)

@when(parsers.parse("I select end date as {days} days from now"))
def select_end_date(assign_leave_page, days):
    assign_leave_page.select_end_date(days)