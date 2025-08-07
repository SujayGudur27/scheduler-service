from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    schedule = Column(String)  # e.g., 'cron:0 9 * * 1' for every Monday 9AM
    last_run = Column(DateTime, nullable=True)
    next_run = Column(DateTime, nullable=True)