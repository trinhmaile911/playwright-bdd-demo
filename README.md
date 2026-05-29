# Playwright BDD Test Framework

Automated testing framework using Playwright, Pytest, and BDD (Behavior-Driven Development) for OrangeHRM application.

## 🚀 Features

- ✅ BDD with Gherkin syntax (pytest-bdd)
- ✅ Page Object Model (POM) design pattern
- ✅ API testing with Playwright's API client
- ✅ Automatic test data cleanup
- ✅ Session management with authenticated context
- ✅ HTML test reports
- ✅ Parallel test execution support
- ✅ GitHub Actions CI/CD integration

## 📁 Project Structure

```
playwright-bdd-demo/
├── .github/
│   └── workflows/
│       └── playwright-tests.yml    # CI/CD workflow
├── config/
│   └── settings.py                 # Configuration settings
├── features/
│   └── admin_module/               # BDD feature files
│       ├── add_user_page.feature
│       └── user_management_page.feature
├── pages/                          # Page Object Models
│   ├── add_user_page.py
│   ├── dashboard_page.py
│   └── user_management_page.py
├── steps/                          # Step definitions
│   ├── admin_module_steps.py       # Step implementations
│   └── test_admin_module.py        # Feature binding
├── utils/
│   └── APIUtils.py                 # API helper methods
├── conftest.py                     # Pytest fixtures
├── pytest.ini                      # Pytest configuration
├── requirements.txt                # Python dependencies
└── .env                            # Environment variables (not in git)
```

## 🛠️ Setup

### Prerequisites

- Python 3.11+ 
- pip

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd playwright-bdd-demo
```

2. Create virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
playwright install chromium
```

4. Create `.env` file:
```bash
cp .env.example .env
# Edit .env with your credentials
```

Example `.env`:
```
BASE_URL=https://opensource-demo.orangehrmlive.com
ADMIN_USERNAME=Admin
ADMIN_PASSWORD=admin123
HEADLESS=true
```

## 🧪 Running Tests

### Run all tests:
```bash
pytest steps/test_admin_module.py -v
```

### Run with HTML report:
```bash
pytest steps/test_admin_module.py -v --html=report.html --self-contained-html
```

### Run smoke tests only:
```bash
pytest steps/test_admin_module.py -m smoke -v
```

### Run tests in parallel:
```bash
pytest steps/test_admin_module.py -n 3
```

### Run in headed mode (see browser):
```bash
# Set HEADLESS=false in .env, then:
pytest steps/test_admin_module.py -v
```

### Run specific scenario:
```bash
pytest steps/test_admin_module.py::test_successfully_add_a_user -v
```

## 📊 Test Reports

After running tests with `--html` flag, open `report.html` in a browser to view detailed test results.

## 🔄 CI/CD

Tests run automatically on GitHub Actions:
- On push to `main`, `master`, or `develop` branches
- On pull requests to these branches
- Can be triggered manually from Actions tab

View workflow configuration: `.github/workflows/playwright-tests.yml`

## 🏗️ Architecture

### BDD Pattern
- **Feature files**: Define test scenarios in Gherkin
- **Step definitions**: Implement scenario steps
- **Page Objects**: Encapsulate page interactions

### Fixtures
- **Browser & Auth**: Shared authenticated session
- **API Context**: Authenticated API client
- **Scenario Context**: Share data between steps
- **Auto Cleanup**: Delete test users after tests

## 📝 Writing Tests

### 1. Add Feature File
```gherkin
Feature: New Feature
  Scenario: Test scenario
    Given I am logged in
    When I perform action
    Then I should see result
```

### 2. Implement Steps
```python
@when("I perform action")
def perform_action(page_object):
    page_object.do_something()
```

### 3. Run Tests
```bash
pytest steps/test_module.py -v
```

## 🤝 Contributing

1. Create feature branch
2. Add tests
3. Ensure all tests pass
4. Submit pull request

## 📄 License

MIT License

## 📊 Allure Reports

### Generate Allure Report Locally:

1. **Run tests with Allure**:
```bash
pytest steps/test_admin_module.py -v --alluredir=allure-results
```

2. **Generate and open report**:
```bash
allure serve allure-results
```

Or generate static report:
```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

### Install Allure (if not installed):

**macOS**:
```bash
brew install allure
```

**Linux**:
```bash
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

**Windows**:
```bash
scoop install allure
```

### Allure Features:
- ✅ Rich HTML reports with charts and graphs
- ✅ Test execution timeline
- ✅ Test history trends
- ✅ Screenshots and attachments
- ✅ Step-by-step execution details
- ✅ Failed tests categorization

