import pytest
from playwright.sync_api import Page, expect

def test_orangehrm_login_logout(page: Page) -> None:
    # Go to login page
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login with valid credentials
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    # Wait for dashboard page
    page.wait_for_url("**/dashboard/**", timeout=30000)

    # Open user dropdown (dynamic locator instead of hard-coded name)
    page.locator("p.oxd-userdropdown-name").click()

    # Click logout
    page.get_by_role("menuitem", name="Logout").click()

    # Assertions after logout
    expect(page.get_by_role("textbox", name="Username")).to_be_visible(timeout=10000)
    expect(page.locator("form")).to_contain_text("Password")
    expect(page.get_by_role("textbox", name="Username")).to_be_empty()
