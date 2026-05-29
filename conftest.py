import pytest
from config.settings import BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD, HEADLESS

from pages.dashboard_page import DashboardPage
from pages.user_management_page import UserManagementPage
from pages.add_user_page import AddUserPage
from utils.APIUtils import APIUtils

@pytest.fixture(scope='session')
def browser(playwright):
    browser = playwright.chromium.launch(headless=HEADLESS)
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
def api_request_context(playwright, auth_context):
    context = playwright.request.new_context(
        base_url=BASE_URL,
        storage_state=auth_context.storage_state(),
        extra_http_headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    )

    yield context

    context.dispose()

@pytest.fixture
def scenario_context():
    return {}

@pytest.fixture
def created_system_users(api_utils):
    user_ids = []

    yield user_ids

    if user_ids:
        api_utils.delete_system_users(user_ids)

@pytest.fixture
def api_utils(api_request_context):
    return APIUtils(api_request_context)

@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)

@pytest.fixture
def user_management_page(page):
    return UserManagementPage(page)

@pytest.fixture
def add_user_page(page):
    return AddUserPage(page)