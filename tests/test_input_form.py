from playwright.sync_api import sync_playwright, expect
from ..config import URL, MESSAGE

def test_input_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL)
        page.click("text=Input Form Submit")
        page.click("button:has-text('Submit')")
        assert page.locator("[name='name']").get_attribute("required")
        page.fill("[name='name']", "John Doe")
        page.fill("[name='email']", "john.doe@example.com")
        page.select_option("[name='country']", "United States")
        page.click("button:has-text('Submit')")
        expect(page.locator(".success-msg")).to_have_text("Thanks for contacting us")
        browser.close()
