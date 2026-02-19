from pydantic import BaseModel
from datetime import datetime
from typing import Optional,Literal

class ScarpeJob(BaseModel):
    job_id : str
    target_url : str
    status: Literal["Pending", "Running", "Completed","Failed"]
    created_at : datetime
    completed_at : Optional[datetime]= None
    result_summary : Optional[dict] = None

