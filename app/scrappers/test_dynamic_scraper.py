from app.scrappers.base_dynamic_scraper import BaseDynamicScraper

if __name__ == "__main__":
    scraper = BaseDynamicScraper()
    html = scraper.fetch_rendered_html("https://news.ycombinator.com")

    print(html[:1000])  # Print the first 1000 characters of the rendered HTML
