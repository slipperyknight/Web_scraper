from fastapi import FastAPI

app = FastAPI(
    title="Dynamic Web Scraper",
    version="0.1.0"
)

@app.get("/ping")
def ping():
    return {"status": "alive"}
