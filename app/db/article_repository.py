from pymongo.errors import DuplicateKeyError
from app.db.mongo import articles_collection
from app.models.article import Article

def save_articles(article: Article) -> bool:
    try:
        articles_collection.insert_one(article.model_dump(mode="json"))
        return True
    except DuplicateKeyError:
        return False
def get_all_articles() -> list[dict]:
    return list(articles_collection.find({},{"_id":0}))
