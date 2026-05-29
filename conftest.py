import pytest
from playwright.sync_api import sync_playwright, expect
from config.settings import BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD, HEADLESS

from pages.dashboard_page import DashboardPage
from pages.user_management_page import UserManagementPage
from pages.add_user_page import AddUserPage

@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        yield browser
        browser.close()

@pytest.fixture(scope='session')
def auth_context(browser):
    context = browser.new_context(base_url=BASE_URL)
    page = context.new_page()

    page.goto('/web/index.php/auth/login')
    page.get_by_placeholder('Username').fill(ADMIN_USERNAME)
    page.get_by_placeholder('Password').fill(ADMIN_PASSWORD)
    page.get_by_role('button', name='Login').click()
    page.wait_for_url("**/dashboard/index")

    yield context
    context.close()

@pytest.fixture
def page(auth_context):
    page = auth_context.new_page()

    yield page
    page.close()

@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)

@pytest.fixture
def user_management_page(page):
    return UserManagementPage(page)

@pytest.fixture
def add_user_page(page):
    return AddUserPage(page)