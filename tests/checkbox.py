import pytest
from playwright.sync_api import sync_playwright, expect
def test_checkbox(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    checkbox = page.locator("input[type='checkbox']:nth-child()")
    # Check the checkbox
    checkbox.check()
    # Assert the checkbox is checked
    expect(checkbox).to_be_checked()
    # Uncheck the checkbox
    checkbox.uncheck()
    # Assert the checkbox is unchecked
    expect(checkbox).not_to_be_checked()
    page.close()