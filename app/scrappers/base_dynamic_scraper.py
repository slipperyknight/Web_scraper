from playwright.sync_api import sync_playwright
#its function is to fetch the rendered HTML content of a webpage using a headless browser. It uses Playwright to launch a headless Chromium browser, navigate to the specified URL, wait for the page to load and for network activity to settle down, and then retrieves the rendered HTML content. Finally, it closes the browser and returns the HTML as a string.
class BaseDynamicScraper: 
    '''
    responsible only for:
    - Launching a headless browser
    - Rendering dynamic pages
    - Returning the rendered HTML content
    '''

    def fetch_rendered_html(self, url: str)-> str:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless = True)

            page = browser.new_page()
            page.goto(url, timeout = 60000)  # wait up to 60 seconds for the page to load
            #wait until js network activity settles down
            page.wait_for_load_state("networkidle")

            html = page.content()

            browser.close()

            return html

