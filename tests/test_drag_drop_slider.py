from playwright.sync_api import sync_playwright, expect
from ..config import URL, MESSAGE

def test_drag_drop_slider():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL)
        page.click("text=Drag & Drop Sliders")
        slider = page.locator("input[value='15']")
        slider.fill("95")
        expect(page.locator("#range")).to_have_text("95")
        browser.close()
