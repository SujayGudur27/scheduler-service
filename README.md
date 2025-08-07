# Scheduler Microservice

A Python-based FastAPI microservice to schedule and manage jobs with RESTful APIs.

## Features
- Create scheduled jobs (e.g., "Run every Monday at 9 AM")
- View all jobs or individual job details
- APScheduler integration for dummy job execution
- SQLite database for persistence
- Fully modular and scalable codebase

## Run the Project

```bash
uvicorn app.main:app --reload
```

## API Endpoints
- `POST /jobs`: Create a new job
- `GET /jobs`: List all jobs
- `GET /jobs/{id}`: Get details of a job

## Example JSON (for POST /jobs)
```json
{
  "name": "Weekly Email Report",
  "description": "Send weekly email every Monday at 9 AM",
  "schedule": "cron:0 9 * * 1"
}
```