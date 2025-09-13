import pytest
import os
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(context, request):
    page = context.new_page()

    # Ensure output folder exists
    os.makedirs("test_results", exist_ok=True)

    # Start tracing before test
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield page

    # Stop tracing after test (always save trace for debugging)
    test_name = request.node.name
    trace_path = f"test_results/{test_name}_trace.zip"
    context.tracing.stop(path=trace_path)

    print(f"Trace saved at: {trace_path}")

    page.close()
