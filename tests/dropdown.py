import pytest
from playwright.sync_api import sync_playwright, expect
def test_dropdown(page):
    page.goto("https://the-internet.herokuapp.com/dropdown")

    dropdown = page.locator("select#dropdown")    
    # Select option by value
    dropdown.select_option("1")  # Selects "Option 1"
    # Assert the selected option
    expect(dropdown).to_have_value("1")
    # Select option by label
    dropdown.select_option(label="Option 2")
    # Assert the selected option
    expect(dropdown).to_have_value("2")
    page.close()