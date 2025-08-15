from playwright.sync_api import sync_playwright, expect

def test_hard_assertions_opencart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Run in headed mode for visibility
        page = browser.new_page()
        page.goto("https://naveenautomationlabs.com/opencart/index.php?route=common/home")
        
        # Hard assertion: Check page title (fails if not exact match, stops test)
        expect(page).to_have_title("Your Store")  # This should pass
        
        # Hard assertion: Check if search input is visible (continues only if previous passes)
        search_locator = page.locator("#search input")
        expect(search_locator).to_be_visible()
        
        # If both pass, the test completes successfully
        print("All hard assertions passed!")
        browser.close()
