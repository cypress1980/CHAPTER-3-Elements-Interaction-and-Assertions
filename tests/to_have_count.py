from playwright.sync_api import sync_playwright, expect

def test_element_focused():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
       # Navigate to the website and log in
        page.goto("https://shop.qaautomationlabs.com/")
        page.fill("input[type='email']", "demo")
        page.fill("input[type='password']", "demo")
        page.click("button[type='submit']")
        
        # Assertion: Verify there are 6 products in the product listing
        products = page.locator("#productContainer")
        expect(products).to_have_count(1)
        
        print("Count assertion passed: Exactly 6 products are present.")
        browser.close()