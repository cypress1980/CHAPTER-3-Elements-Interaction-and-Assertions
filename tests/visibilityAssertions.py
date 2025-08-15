from playwright.sync_api import sync_playwright, expect

def test_visibility_assertion():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to the website
        page.goto("https://shop.qaautomationlabs.com/")
        
        # Perform login
        page.fill("input[type='email']", "demo")
        page.fill("input[type='password']", "demo")
        page.click("button[type='submit']")
        
        # Visibility assertion: Check if the "Add to Cart" button is visible
        add_to_cart_button = page.locator("button:has-text('Add to cart')").first
        expect(add_to_cart_button).to_be_visible()
        
        browser.close()