from pytest_bdd import then
from playwright.sync_api import expect

TOAST_SELECTOR = ".oxd-toast"

@then("I should see a toast message")
def assert_toast_message(page):
    expect(page.locator(TOAST_SELECTOR)).to_be_visible()