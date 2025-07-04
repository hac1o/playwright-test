from playwright.sync_api import Page


def test_cielo_breez_edge_pro_page_loads(page: Page):
    print("Navigating to CieloWigle homepage...")
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