#  Scheduler Microservice

A Python-based FastAPI microservice to schedule and manage jobs using RESTful APIs. This service allows users to create, view, and manage scheduled jobs with customizable execution intervals using `APScheduler`.

---

##  Features

-  Create jobs with flexible cron schedules (e.g., every Monday at 9 AM)
-  View all scheduled jobs or fetch one by ID
-  Job execution simulated using dummy task (prints to console)
-  APScheduler integration for background job handling
-  SQLite database for persistent storage
-  Modular, scalable, and SOLID-compliant codebase
---

## Tech Stack

- **Backend:** FastAPI
- **Scheduler:** APScheduler
- **ORM:** SQLAlchemy
- **Database:** SQLite
- **Language:** Python 3.10+

---

## How to Run the Project

1. **Clone the repository:**
```bash
git clone https://github.com/SujayGudur27/scheduler-service.git
cd scheduler-service
```

2. **Create a virtual environment:**
```bash
python -m venv venv
.env\Scriptsctivate  # For Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the API server:**
```bash
uvicorn app.main:app --reload
```

5. **Access Swagger UI:**
Visit [http://localhost:8000/docs](http://localhost:8000/docs) in your browser

---

##  API Endpoints

| Method | Endpoint        | Description                |
|--------|------------------|----------------------------|
| POST   | `/jobs`         | Create a new job           |
| GET    | `/jobs`         | List all jobs              |
| GET    | `/jobs/{id}`    | Get details of a specific job |

---

##  Example Request Body (POST /jobs)

```json
{
  "name": "Weekly Email Report",
  "description": "Send weekly email every Monday at 9 AM",
  "schedule": "cron:0 9 * * 1"
}
```

>  The `schedule` follows cron format.  
> Example above runs **every Monday at 9:00 AM**

---

##  One-Pager: Scaling Strategy

To scale this service to handle **~10,000 users**, **1,000+ services**, and **6,000+ API requests/minute**, we would:

### 1. Microservices Architecture
- Split into multiple services:
  - Job Management API
  - Job Execution Worker
  - Job History Logger

### 2.  Distributed Job Queue
- Use **Celery** + **Redis** (or RabbitMQ) to manage job dispatching across workers
- Allows horizontal scaling of background workers

### 3.  Scalable Database
- Switch from SQLite to **PostgreSQL**
- Add read replicas and connection pooling (e.g., PgBouncer)

### 4.  API Gateway & Load Balancing
- Deploy behind **NGINX / AWS API Gateway / Kong**
- Rate limiting, authentication, caching

### 5.  Cloud-native Deployment
- Dockerize services
- Deploy with **Kubernetes** for orchestration and auto-scaling

### 6. Observability & Logging
- Use **Prometheus + Grafana** for metrics
- Centralized logs via **ELK stack** (Elasticsearch, Logstash, Kibana)

---

