from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from app.crud import get_all_jobs
from app.database import SessionLocal
from datetime import datetime

scheduler = BackgroundScheduler()

def dummy_job(job_id: int, job_name: str):
    print(f"[{datetime.now()}] Running job {job_id}: {job_name}")

def start():
    db = SessionLocal()
    jobs = get_all_jobs(db)
    for job in jobs:
        if job.schedule.startswith("cron:"):
            cron_expr = job.schedule.replace("cron:", "")
            trigger = CronTrigger.from_crontab(cron_expr)
            scheduler.add_job(dummy_job, trigger, args=[job.id, job.name], id=str(job.id), replace_existing=True)
    scheduler.start()