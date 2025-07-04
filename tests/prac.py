from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    print("Launching browser...")
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    
    # Start tracing for debugging
    context.tracing.start(screenshots=True, snapshots=True)

    page = context.new_page()
    page.goto("https://cielowigle.com/ ")

    print("Clicking 'Order Now'...")
    page.get_by_role("link", name="Order Now").click()

    print("Waiting for popup...")
    with page.expect_popup() as page2_info:
        page.get_by_role("link", name="Order Now").click()
    page2 = page2_info.value

    print("Searching DiversiTech...")
    page2.goto("https://www.diversitech.com/product/search?keyword=cielo")

    print("Clicking Cielo Breez Edge Pro...")
    page2.get_by_role("link", name="Cielo Breez Edge Pro: Premium").click()

    print("Asserting heading visibility...")
    heading = page2.get_by_role("heading", name="Cielo Breez Edge Pro: Premium")
    assert heading.is_visible(), "Product heading not visible!"

    print("✅ Test completed successfully!")

    # Stop tracing and save trace.zip
    context.tracing.stop(path="test-results/trace.zip")

    context.close()
    browser.close()