from playwright.sync_api import sync_playwright
import pytest

def test_xpath_selector():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://testing.qaautomationlabs.com/web-table.php")
        # Wait for the table cell to be ready
        page.wait_for_selector("//table//tr[2]/td[2]")
        # Find the cell using XPath and get its text
        cell = page.locator("//table//tr[2]/td[2]")
        text = cell.inner_text()
        print(f"Cell content Is ==> : {text}")
        browser.close()
