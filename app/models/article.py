from pydantic import BaseModel, HttpUrl
from datetime import datetime

class Article(BaseModel):
    title: str
    url : HttpUrl
    source: str
    scraped_at: datetime
    
