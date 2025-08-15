from playwright.sync_api import sync_playwright, expect

def test_presence_assertion():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to the website
        page.goto("https://shop.qaautomationlabs.com/")
        
        # Perform login
        page.fill("input[type='email']", "demo")
        page.fill("input[type='password']", "demo")
        page.click("button[type='submit']")
        
        # Presence assertion: Check if product listing section is present
        product_list = page.locator("ul.products")
        expect(product_list).to_have_count(1)  # Ensures the product list exists
        
        print("Presence assertion passed: Product listing section is present.")
        browser.close()