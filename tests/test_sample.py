def test_exampe():
    assert 1+1 == 2

    import pytest
from playwright.sync_api import sync_playwright

def test_google_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://google.com")
        title = page.title()
        assert "Google" in title
        browser.close()