import pytest_check as check
from playwright.sync_api import sync_playwright, expect

def test_soft_assertions_opencart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://naveenautomationlabs.com/opencart/index.php?route=common/home")
   
    # Soft Assertion 1: Page title
        check.equal(page.title(), "Your Store", "Page title mismatch")

    # Soft Assertion 2: Logo visibility
        logo = page.locator("img[title='naveenopencart']")
        check.is_true(logo.is_visible(), "Logo should be visible on homepage")

    # Soft Assertion 3: Search box placeholder
        search_placeholder = page.locator("input[name='search']").get_attribute("placeholder")
        check.equal(search_placeholder, "SearchUpdated", "Search placeholder text mismatch")
        
    # Soft Assertion 4: Search box placeholder
        enterData_searchBox = page.locator("input[name='search']")
        enterData_searchBox.fill("NaveenAutomationLabs")
        value =enterData_searchBox.input_value()
        check.equal(value, "NaveenAutomationLabs")
        page.wait_for_timeout(2000)

        browser.close()
