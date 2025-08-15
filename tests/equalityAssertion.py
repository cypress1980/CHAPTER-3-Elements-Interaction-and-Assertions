from playwright.sync_api import sync_playwright
import pytest

def test_equality_assertion():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to the login page
        page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
        
        # Fill in login credentials
        page.fill("input[name='email']", "timcook@yopmail.com")
        page.fill("input[name='password']", "Test@1234")
        page.click("input[value='Login']")
        
        # Equality Assertion: Verify the page title
        expected_title = "My Account"
        actual_title = page.title()
        assert actual_title == expected_title, f"Expected page title '{expected_title}', but got '{actual_title}'"
        
        browser.close()