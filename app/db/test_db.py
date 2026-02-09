from datetime import datetime,timezone

from app.scrappers.base_dynamic_scraper import BaseDynamicScraper
from app.core.article_parser import ArticleParser
from app.core.validator import validate_articles
from app.models.article import Article
from app.db.article_repository import save_articles, get_all_articles

if __name__ == "__main__":
    scraper = BaseDynamicScraper()
    parser = ArticleParser()

    html = scraper.fetch_rendered_html("https://news.ycombinator.com")
    raw_articles = parser.parse(html)
    valid_articles = validate_articles(raw_articles)

    saved = 0
    skipped = 0

    for a in valid_articles:
        article = Article(
            title = a["title"],
            url = a["url"],
            source = a["source"],
            scraped_at= datetime.now(timezone.utc)
        )

        if save_articles(article):
            saved += 1
        else:
            skipped += 1
    print(f"Saved: {saved}")
    print(f"Skipped(duplicates):{skipped}")

    print("\n Stored Articles in DB:")
    for doc in get_all_articles()[:5]:
        print(doc)
    
