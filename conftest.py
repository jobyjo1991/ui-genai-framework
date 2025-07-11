# conftest.py

import os
import pytest
from datetime import datetime
from playwright.sync_api import sync_playwright

# --- FIXTURES ---

@pytest.fixture(scope="session")
def playwright_browser():
    """Starts and stops the Playwright browser session"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(playwright_browser):
    """Provides a fresh browser context and page per test"""
    context = playwright_browser.new_context()
    page = context.new_page()
    yield page
    context.close()

# --- UTILITY FIXTURE ---

@pytest.fixture(scope="function", autouse=True)
def log_test_start_and_end(request):
    """Logs when each test starts and ends"""
    test_name = request.node.name
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[LOG] Starting test: {test_name} at {start_time}")

    yield

    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[LOG] Finished test: {test_name} at {end_time}")

# --- PLACEHOLDER FOR GENAI INTEGRATION ---

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_teardown(item, nextitem):
    """Optional: Placeholder to summarize results after each test"""
    test_result = item.name
    # TODO: Pass actual test status to summarize with GenAI
    # from utils.genai_helper import summarize_test_results
    # print(summarize_test_results(test_result))
    pass
