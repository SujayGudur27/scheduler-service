from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JobBase(BaseModel):
    name: str
    description: Optional[str] = None
    schedule: str

class JobCreate(JobBase):
    pass

class JobResponse(JobBase):
    id: int
    last_run: Optional[datetime]
    next_run: Optional[datetime]

    class Config:
        orm_mode = True