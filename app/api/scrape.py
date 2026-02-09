from fastapi import APIRouter
from datetime import datetime,timezone
from app.scrappers.base_dynamic_scraper import BaseDynamicScraper
from app.core.article_parser import ArticleParser
from app.core.validator import validate_articles
from app.models.article import Article
from app.db.article_repository import save_articles

router = APIRouter(prefix="/scrape", tags=["scraping"])

@router.post("/hn")

def scrape_hacker_news():
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
            scraped_at = datetime.now(timezone.utc)
        )
        if save_articles(article):
            saved += 1
        else:
            skipped += 1
    
    return{
        "status":"success",
        "source" : "Hacker News",
        "raw_articles": len(raw_articles),
        "valid_articles": len(valid_articles),
        "saved": saved,
        "skipped_duplicates": skipped
    }

