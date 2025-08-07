from fastapi import FastAPI
from app.database import engine, Base
from app import api, scheduler

app = FastAPI(title="Scheduler Microservice", version="1.0.0")

Base.metadata.create_all(bind=engine)

# Include API routes
app.include_router(api.router)

# Start scheduler on startup
@app.on_event("startup")
def start_scheduler():
    scheduler.start()