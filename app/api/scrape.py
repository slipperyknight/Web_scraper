from fastapi import APIRouter
from datetime import datetime,timezone
from app.scrappers.base_dynamic_scraper import BaseDynamicScraper
from app.core.article_parser import ArticleParser
from app.core.validator import validate_articles
from app.models.article import Article
from app.db.article_repository import save_articles
from app.models.scrape_request import ScraperRequest
from app.core.url_utils import normalize_url
from fastapi import HTTPException

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
@router.post("/article")
def scrape_article(req: ScraperRequest):
    url = normalize_url(str(req.url))

    scraper = BaseDynamicScraper()
    parser = ArticleParser()

    try:
        html = scraper.fetch_rendered_html(url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"failed to load the page")
    
    raw_articles = parser.parse(html)
    valid_articles = validate_articles(raw_articles)

    if not valid_articles:
        raise HTTPException(status_code=422, detail="No valid articles found on the page")
    
    saved = 0
    skipped =0

    for a in valid_articles:
        article = Article(
            title = a["title"],
            url = a["url"],
            source = url,           
            scraped_at = datetime.now(timezone.utc)
        )
        if save_articles(article):
            saved += 1
        else:
            skipped += 1
    return {
        "status":"success",
        "source": url,
        "raw_articles": len(raw_articles),
        "valid_articles": len(valid_articles),
        "saved": saved,
        "skipped_duplicates": skipped
    }




