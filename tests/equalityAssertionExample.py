from playwright.sync_api import sync_playwright, expect

def test_equality_assertion():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page() 
        
        # Navigate to the website
        page.goto("https://shop.qaautomationlabs.com/")
        
        # Perform login
        page.fill("input[type='email']", "demo")
        page.fill("input[type='password']", "demo")
        page.click("button[type='submit']")
        
        # Equality assertion: Check if the page title is as expected
        expected_title = "SHOP | QA AUTOMATIONLAB"
        actual_title = page.title()
        assert actual_title == expected_title, f"Expected page title '{expected_title}', but got '{actual_title}'"
        browser.close()