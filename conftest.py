
import allure
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright
from config.settings import BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD, HEADLESS
from pages.assign_leave_page import AssignLeavePage

from pages.dashboard_page import DashboardPage
from pages.personal_details_page import PersonalDetailsPage
from pages.user_management_page import UserManagementPage
from pages.add_user_page import AddUserPage
from utils.api_utils import APIUtils
from utils.json_helper import load_test_data

AUTH_FILE = Path("tests/.auth/admin.json")

@pytest.fixture(scope='session', autouse=True)
def authenticate():
    AUTH_FILE.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        context = browser.new_context(base_url=BASE_URL)
        page = context.new_page()

        page.goto('/web/index.php/auth/login')
        page.get_by_placeholder('Username').fill(ADMIN_USERNAME)
        page.get_by_placeholder('Password').fill(ADMIN_PASSWORD)
        page.get_by_role('button', name='Login').click()
        page.wait_for_url("**/dashboard/index")

        context.storage_state(path=AUTH_FILE)
        browser.close()

@pytest.fixture(scope='session')
def browser(playwright):
    browser = playwright.chromium.launch(headless=HEADLESS, args=["--start-maximized"])
    yield browser
    browser.close()

@pytest.fixture(scope='session')
def auth_context(browser, authenticate):
    context = browser.new_context(
        base_url=BASE_URL,
        storage_state=AUTH_FILE,
        no_viewport=True,
    )
    yield context
    context.close()

@pytest.fixture
def page(auth_context, request):
    page = auth_context.new_page()
    request.node._playwright_page = page
    yield page
    page.close()

@pytest.fixture
def api_request_context(playwright, auth_context):
    context = playwright.request.new_context(
        base_url=BASE_URL,
        storage_state=AUTH_FILE,  # 👈 dùng file thay vì auth_context.storage_state()
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

@pytest.fixture
def assign_leave_page(page):
    return AssignLeavePage(page)

@pytest.fixture
def personal_details_page(page):
    return PersonalDetailsPage(page)

@pytest.fixture
def personal_details_data():
    return load_test_data("personal_details.json")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = getattr(item, "_playwright_page", None)

        if page:
            try:
                allure.attach(
                    page.screenshot(full_page=True),
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception as e:
                print(f"Failed to attach screenshot: {e}")