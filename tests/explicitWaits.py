from playwright.sync_api import sync_playwright


def test_auto_wait():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.amazon.in")

        # Step 1: Type a query into the search bar
        page.fill("input#twotabsearchtextbox", "laptop")

        # Step 2: Click on the search button
        page.click("input#nav-search-submit-button")

        # Step 3: Wait for search results to load
        page.wait_for_selector("div.s-main-slot div[data-component-type='s-search-result']", timeout=10000)

        # Step 4: Get and print the title of the first listed product
        first_product = page.locator("div.s-main-slot div[data-component-type='s-search-result'] h2 span").first
        print("First Product Title:", first_product.inner_text())

        browser.close()
