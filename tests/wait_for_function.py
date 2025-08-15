from playwright.sync_api import sync_playwright, expect

def test_element_text():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.amazon.in")

        # Wait until the button is enabled using JS
        page.wait_for_function(
            """() => {
                const btn = document.querySelector("input#nav-search-submit1-button");
                return btn && !btn.disabled;
            }"""
        )
        page.click("input#nav-search-submit-button")
        print("Clicked search button!")
        browser.close()