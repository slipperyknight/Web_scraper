from app.db.mongo import jobs_collection
from app.models.scrape_job import ScrapeJob


def create_job(job: ScrapeJob):
    jobs_collection.insert_one(job.model_dump())


def update_job(job_id: str, updates: dict):
    jobs_collection.update_one(
        {"job_id": job_id},
        {"$set": updates}
    )


def get_job(job_id: str):
    return jobs_collection.find_one(
        {"job_id": job_id},
        {"_id": 0}
    )
