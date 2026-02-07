from app.scrappers.base_dynamic_scraper import BaseDynamicScraper
from app.core.article_parser import ArticleParser
from app.core.validator import validate_articles

if __name__ == "__main__":
    scraper = BaseDynamicScraper()
    parser = ArticleParser()

    html = scraper.fetch_rendered_html("https://news.ycombinator.com")
    raw_articles = parser.parse(html)
    valid_articles = validate_articles(raw_articles)


    print(f"Raw Articles: {len(raw_articles)} ")
    print(f"Valid Articles: {len(valid_articles)}\n")
    
    for article in valid_articles[:5]: # Print the first 5 articles to verify the parsing results
        print(article)

