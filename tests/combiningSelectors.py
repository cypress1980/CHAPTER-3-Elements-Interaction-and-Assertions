from playwright.sync_api import sync_playwright
import pytest

def test_combine_selector():
    with sync_playwright() as p:
     browser = p.chromium.launch(headless=False)
     page = browser.new_page()
     page.goto("https://testing.qaautomationlabs.com/dropdown.php")
    
    # Combine CSS and text for dropdown selection
     dropdown = page.locator("#fruitDropdown")
     dropdown.select_option(label="Banana")
     print("Selected Option 2 : Banana from dropdown!")
     browser.close()