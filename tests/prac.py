from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    print("Launching browser...")
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # --- Step 1: Navigate to CieloWigle ---
    print("Going to cielowigle.com...")
    page.goto("https://cielowigle.com/ ", wait_until="domcontentloaded")
    
    # Ensure page is fully loaded and link is visible
    order_now_locator = page.get_by_role("link", name="Order Now", exact=True)
    order_now_locator.wait_for_state("visible")
    order_now_locator.click()

    # --- Step 2: Wait for Popup Page ---
    print("Waiting for popup...")
    with page.expect_popup() as page2_info:
        page.get_by_role("link", name="Order Now", exact=True).click()
    page2 = page2_info.value

    # Wait for new page to load
    page2.wait_for_load_state("networkidle")

    # --- Step 3: Search DiversiTech ---
    print("Searching DiversiTech...")
    page2.goto("https://www.diversitech.com/product/search?keyword=cielo")
    
    # Wait for product list to load
    page2.wait_for_selector("a.product-tile-inner")

    # --- Step 4: Click Product Link ---
    print("Clicking Cielo Breez Edge Pro...")
    product_link = page2.get_by_role("link", name="Cielo Breez Edge Pro: Premium")
    product_link.wait_for_state("visible")
    product_link.click()

    # --- Step 5: Assertion ---
    print("Asserting heading visibility...")
    heading = page2.get_by_role("heading", name="Cielo Breez Edge Pro: Premium")
    heading.wait_for_state("visible")
    expect(heading).to_be_visible()

    print("✅ Test completed successfully!")

    # --- Cleanup ---
    context.close()
    browser.close()