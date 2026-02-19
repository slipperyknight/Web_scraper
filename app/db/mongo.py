from pymongo import MongoClient, ASCENDING

#create a MongoDB client and connect to the database
client = MongoClient("mongodb://localhost:27017/")

#database and collection
db = client["web_scraper"]
articles_collection = db["articles"]

#create an index to prenvent duplication
articles_collection.create_index(
    [("title",ASCENDING),("source",ASCENDING)],
    unique = True   
)

jobs_collection = db["scrape_jobs"]
