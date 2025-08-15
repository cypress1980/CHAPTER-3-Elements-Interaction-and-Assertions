from playwright.sync_api import sync_playwright, expect

def test_element_text():
    with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      page = browser.new_page()
      page.goto("https://www.amazon.in")

      # Enter search query and submit
      page.fill("input#twotabsearchtextbox", "laptop")
      page.click("input#nav-search-submit-button")

      # Wait for search results URL to load
      page.wait_for_url("**/s?k=laptop*")
      print("Navigated to search results for laptop!")

      browser.close()