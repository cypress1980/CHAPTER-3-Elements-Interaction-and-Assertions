from playwright.sync_api import sync_playwright
import pytest

def test_testBased_selector():
    with sync_playwright() as p:
     browser = p.chromium.launch(headless=False)
     page = browser.new_page()
     page.goto("https://testing.qaautomationlabs.com/radio-button.php")
    
    # Find radio button by text
     radio_Button_2 = page.locator('text=  Radio Button 2')
     radio_Button_2.check()
     page.wait_for_timeout(2000)  # Wait for a second to see the effect
    
     print("Hi !! 'Radio Button 2 is selected button!")
     browser.close()