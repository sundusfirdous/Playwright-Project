# Playwright Demo Project

## High-Level Design

This project is a test automation framework using Playwright and Pytest for end-to-end testing of web applications. The main goals are:
- Automate browser interactions and UI validations
- Organize tests and page objects for maintainability
- Generate HTML reports for test results

### Main Components
- **Test Scripts**: Located in the `tests/` folder, each script validates a specific feature or flow.
- **Page Objects**: Located in the `pages/` folder, encapsulate UI element locators and actions for each page.
- **Test Data**: Stored in `test_data/` for data-driven testing.
- **Reports**: HTML reports generated in `reports/` after test runs.
- **Configuration**: `pytest.ini` for test options and Playwright settings.

## Low-Level Design

### Folder Structure
- `tests/` — Contains all test scripts (e.g., login, API, data-driven tests)
- `pages/` — Page Object Model classes for each web page
- `test_data/` — CSV/JSON files for test data
- `reports/` — Test result reports
- `utils/` — Utility/helper functions (if any)
- `requirements.txt` — Python dependencies
- `pytest.ini` — Pytest and Playwright configuration

### Example Test Flow
1. **Test Initialization**: Pytest discovers and runs test scripts in `tests/`.
2. **Browser Launch**: Playwright launches the browser (Chromium, headed/headless as per config).
3. **Page Object Usage**: Test scripts use page objects to interact with UI elements.
4. **Assertions**: Playwright's `expect` is used for UI validations.
5. **Reporting**: After execution, HTML reports are generated in `reports/`.

### Sample Page Object (pages/orangehrm_home_page.py)
```python
class HomePage:
    def __init__(self, page):
        self.page = page
        self.upgrade_button = page.get_by_role("button", name="Upgrade")
    def is_upgrade_button_visible(self):
        expect(self.upgrade_button).to_be_visible()
```

### Sample Test (tests/test_login_orangehrm.py)
```python
def test_example(page: Page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    home_page.is_upgrade_button_visible()
```

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Install Playwright browsers: `python -m playwright install`
3. Run tests: `pytest`

## Reporting
- HTML reports are generated in `reports/` after each test run.

## Extending
- Add new page objects in `pages/`
- Add new test scripts in `tests/`
- Add test data in `test_data/`

---
For more details, see individual files and comments in the code.
