# Employee Management API

A layered FastAPI application with environment-based configuration, PostgreSQL, Docker Compose, and automated tests.

## Technology Stack

- Python 3.13
- FastAPI
- Pydantic Settings
- PostgreSQL
- Docker and Docker Compose
- Pytest

## Project Structure

```text
employee-management-api/
├── app/
│   ├── api/
│   ├── core/
│   └── main.py
├── contracts/
│   └── api-contract.md
├── docs/
├── sample_data/
│   └── employees.json
├── scripts/
├── tests/
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Prerequisites

Install Docker Desktop and ensure it is running.

## Run the Application

Start the API and PostgreSQL database:

```powershell
docker compose up --build -d
```

Check the running containers:

```powershell
docker compose ps
```

## API Endpoints

Health check:

`GET /api/v1/health`

Interactive API documentation:

http://localhost:8000/docs

## Run Tests

Activate the virtual environment and run:

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

## Stop the Application

```powershell
docker compose down
```

The PostgreSQL data volume is preserved when using this command.