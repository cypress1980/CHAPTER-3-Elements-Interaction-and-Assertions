from playwright.sync_api import sync_playwright, expect

def test_element_text():
    with sync_playwright() as p:
     browser = p.chromium.launch(headless=False)
     page = browser.new_page()
     page.goto("https://www.amazon.in")

    # Wait for the search box to appear (up to 5 seconds)
     page.wait_for_selector("#twotabsearchtextbox", timeout=5000)

     print("Search box is ready!")
     browser.close()