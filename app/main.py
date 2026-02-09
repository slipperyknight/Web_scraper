from fastapi import FastAPI
from app.api.scrape import router as scrape_router

app = FastAPI(
    title="Dynamic Web Scraper",
    version="0.1.0"
)

@app.get("/ping")
def ping():
    return {"status": "alive"}

app.include_router(scrape_router)
