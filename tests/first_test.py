from playwright.sync_api import sync_playwright

def open_webpage(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        input("Press Enter to close the browser...")
        browser.close()

if __name__ == "__main__":
    open_webpage("https://google.com")

    import pytest
from playwright.sync_api import sync_playwright

