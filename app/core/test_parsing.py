from datetime import datetime, timezone
from app.scrappers.base_dynamic_scraper import BaseDynamicScraper
from app.core.article_parser import ArticleParser
from app.core.validator import validate_articles
from app.models.article import Article

if __name__ == "__main__":
    scraper = BaseDynamicScraper()
    parser = ArticleParser()

    html = scraper.fetch_rendered_html("https://news.ycombinator.com")
    raw_articles = parser.parse(html)
    valid_articles = validate_articles(raw_articles)

    article_objects =[]

    for article in valid_articles:
        article_obj = Article(
            title = article["title"],
            url = article["url"],
            source = article["source"],
            scraped_at = datetime.now(timezone.utc)
        )
        article_objects.append(article_obj)
    print(f"final articles : {len(article_objects)}\n")
    for a in article_objects[:5]:
        print(a.model_dump(mode="json"))
        

