from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://demo.guru99.com/test/radio.html")
    
    # Selector from SelectorsHub
    radio_button = page.locator("#vfb-7-1")
    
    # Select the radio button
    radio_button.check()
    
    # Assert the radio button is checked
    expect(radio_button).to_be_checked()
    
    page.close()
    browser.close()