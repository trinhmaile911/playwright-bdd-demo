from pytest_bdd import scenarios
from steps.admin_module_steps import *

# Bind feature files from admin_module
scenarios("../features/admin_module/user_management_page.feature")
scenarios("../features/admin_module/add_user_page.feature")