from datetime import datetime, timezone
from app.scrappers.base_dynamic_scraper import BaseDynamicScraper
from app.core.article_parser import ArticleParser
from app.core.validator import validate_articles
from app.models.article import Article 
from app.db.article_repository import save_articles
from app.db.job_repository import update_job

def run_scrape_job(job_id: str, url : str):
    try:
        update_job(job_id,{"status":"Running"})

        scraper = BaseDynamicScraper()
        parser = ArticleParser()

        html = scraper.fetch_rendered_html(url)
        raw_articles = parser.parse(html)
        valid_articles = validate_articles(raw_articles)
        
        saved = 0
        skipped = 0

        for a in valid_articles:
            article = Article(
                title = a["title"],
                url = a["url"],
                source = url
                scraped_at = datetime.now(timezone.utc)

            )
            if save_articles(article):
                saved += 1
            else:
                skipped += 1
        
        update_job()
