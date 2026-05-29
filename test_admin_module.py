def test_add_user(dashboard_page, user_management_page, add_user_page):
    dashboard_page.navigate_to_dashboard()
    dashboard_page.open_admin_page()
    user_management_page.click_add_user()
    add_user_page.expect_add_user_displayed()


def test_cancel_add_user(dashboard_page, user_management_page, add_user_page):
    dashboard_page.navigate_to_dashboard()
    dashboard_page.open_admin_page()
    user_management_page.click_add_user()
    add_user_page.click_cancel()
    user_management_page.expect_system_users_displayed()