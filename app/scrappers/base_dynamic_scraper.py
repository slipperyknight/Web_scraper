from playwright.sync_api import sync_playwright

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

