from playwright.sync_api import sync_playwright

def test_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)# Launch a headless browser (no GUI)
        page = browser.new_page() #  Open a new page in the browser
        page.goto("https://news.ycombinator.com", timeout=60000) # Wait up to 60 seconds for the page to load
        page.wait_for_load_state("networkidle") # Wait until the network is idle (no more than 2 network connections for at least 500 ms)

        html = page.content() # Get the page content as HTML
        print(html[:1000])  # print first 1000 chars only

        browser.close()

if __name__ == "__main__":
    test_browser()
