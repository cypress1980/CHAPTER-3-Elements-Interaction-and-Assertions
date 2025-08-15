from playwright.sync_api import sync_playwright, expect

def test_element_text():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
     # Navigate to the website and log in
        page.goto("https://shop.qaautomationlabs.com/")
        page.fill("input[type='email']", "demo")
        page.fill("input[type='password']", "demo")
        page.click("button[type='submit']")
        
        # Assertion: Verify the page header has the text "Shop"
        page_header = page.locator("#navbarCollapse")
        expect(page_header).to_contain_text("Shop")
        browser.close()