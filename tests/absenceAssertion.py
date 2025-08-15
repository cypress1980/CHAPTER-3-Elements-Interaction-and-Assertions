from playwright.sync_api import sync_playwright
import pytest

def test_absence_assertion():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to the login page
        page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
        
        # Fill in login credentials
        page.fill("input[name='email']", "timcook@yopmail.com")
        page.fill("input[name='password']", "Test@1234")
        page.click("input[value='Login']")
        
        # Absence Assertion: Ensure no error message is present
        error_message = page.locator(".alert-danger")
        assert error_message.count() == 0, "Login error message should not be present after successful login"
        
        browser.close()