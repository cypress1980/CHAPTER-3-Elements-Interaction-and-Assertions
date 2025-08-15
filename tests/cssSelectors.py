from playwright.sync_api import sync_playwright
import pytest
def test_CSS_ID_Selector():
    with sync_playwright() as p:
     browser = p.chromium.launch(headless=False)
     page = browser.new_page()
     page.goto("https://testing.qaautomationlabs.com/form.php")
    
    # Locate the name input field using CSS ID selector
     name_input = page.locator("#firstname")
     name_input.fill("John Doe")
     page.wait_for_timeout(3000)
     print("Filled the name field successfully!")
     page.close()