from playwright.sync_api import sync_playwright, expect
from config import URL

def test_input_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL)
        page.click("text=Input Form Submit")

        # Try to submit the form without filling details
        page.click("button:has-text('Submit')")

        # Capture the popup alert using Playwright's dialog event
        popup_message = None

        def handle_dialog(dialog):
            nonlocal popup_message
            popup_message = dialog.message
            dialog.dismiss()  # Close the alert automatically

        page.on("dialog", handle_dialog)
        page.click("button:has-text('Submit')")

        assert popup_message == "Please fill out this field.", f"Expected alert message not found. Actual: {popup_message}"

        page.fill("[name='name']", "John Doe")
        page.fill("[name='email']", "john.doe@example.com")
        page.select_option("[name='country']", "United States")
        page.click("button:has-text('Submit')")

        expect(page.locator(".success-msg")).to_have_text("Thanks for contacting us")
        browser.close()
