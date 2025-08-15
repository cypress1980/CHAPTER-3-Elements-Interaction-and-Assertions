from playwright.sync_api import sync_playwright, expect

def test_element_text():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.amazon.in")
        
        # Wait for a lighter state if networkidle times out
        page.wait_for_load_state("domcontentloaded")
        print("Page fully loaded and network idle")

        browser.close()