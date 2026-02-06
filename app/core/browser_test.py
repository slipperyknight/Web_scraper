from playwright.sync_api import sync_playwright

def test_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) # Launch a headless browser
        page = browser.new_page() # Open a new page
        page.goto("https://news.ycombinator.com", timeout=60000) # Navigate to Hacker News with a timeout
        page.wait_for_load_state("networkidle") # Wait until the network is idle

        html = page.content()# Get the page content
        print(html[:1000]) # Print the first 1000 characters of the HTML

        browser.close() # Close the browser
if __name__ == "__main__":
    test_browser()
