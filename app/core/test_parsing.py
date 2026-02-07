from app.scrappers.base_dynamic_scraper import BaseDynamicScraper
from app.core.article_parser import ArticleParser

if __name__ == "__main__":
    scraper = BaseDynamicScraper()
    parser = ArticleParser()

    html = scraper.fetch_rendered_html("https://news.ycombinator.com")
    articles = parser.parse(html)

    print(f"found {len(articles)} articles\n")

    for article in articles[:5]: # Print the first 5 articles to verify the parsing results
        print(article)

