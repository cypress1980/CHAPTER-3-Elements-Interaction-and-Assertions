import pytest
from playwright.sync_api import expect

EXPECTED_URL_AFTER_LOGIN = "https://ecommerce-playground.lambdatest.io/index.php?route=account/account"
def test_login(page):
    # Navigate to the login page
    page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    # Fill in the username and password fields
    page.fill("[id='input-email']", "timcook@yopmail.com")
    page.fill("[id='input-password']", "Test@1234")
    # Click the login button
    page.click("input[type='submit']")
    # Check user logged in successfully
    expect(page).to_have_url(EXPECTED_URL_AFTER_LOGIN)
    expect(page).to_have_title("My Account")
    expect(page.get_by_role("heading", name="My Account")).to_be_visible()