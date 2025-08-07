from sqlalchemy.orm import Session
from app import models, schemas

def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(
        name=job.name,
        description=job.description,
        schedule=job.schedule,
        last_run=None,
        next_run=None
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_all_jobs(db: Session):
    return db.query(models.Job).all()

def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()