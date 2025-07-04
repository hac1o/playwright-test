from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print("Launching browser...")
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    print("Going to cielowigle.com...")
    page.goto(" https://cielowigle.com/ ")  

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
    page2.get_by_role("heading", name="Cielo Breez Edge Pro: Premium").click()

    print("✅ Test completed successfully!")

    # Cleanup
    context.close()
    browser.close()