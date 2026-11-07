# FastAPI Backend Engine

A production-style REST API built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL/SQLite**, implementing JWT authentication, role-based authorization, and CRUD endpoints.

## Features
- **Authentication:** OAuth2 password bearer flow with JWT tokens & bcrypt password hashing.
- **Relational Data Modeling:** SQLAlchemy ORM models with one-to-many relationship (`User` -> `Tasks`).
- **Data Validation:** Strict serialization and request body validation via Pydantic v2.
- **Interactive Documentation:** Automatic Swagger UI at `/docs` and ReDoc at `/redoc`.

## Quickstart

### 1. Create and Activate Virtual Environment
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Server
```bash
uvicorn app.main:app --reload
```

Open your browser and visit: **http://127.0.0.1:8000/docs**

