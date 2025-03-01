from playwright.sync_api import sync_playwright, expect
from config import URL, MESSAGE

def test_simple_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL)
        page.click("text=Simple Form Demo")
        assert "simple-form-demo" in page.url
        page.fill("#user-message", MESSAGE)
        page.click("#showInput")
        expect(page.locator("#message")).to_have_text(MESSAGE)
        browser.close()
