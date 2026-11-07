import sys
from pathlib import Path

# Ensure project root is in sys.path so direct execution works in any IDE
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.session import Base, engine
from app.api.v1.endpoints import auth, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

# Enable CORS for frontend clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["Authentication"])
app.include_router(tasks.router, prefix=f"{settings.API_V1_STR}/tasks", tags=["Tasks"])

@app.get("/")
def health_check():
    return {"status": "healthy", "service": settings.PROJECT_NAME}

if __name__ == "__main__":
    import uvicorn
    print("\n[+] Starting FastAPI Backend Engine at http://127.0.0.1:8000")
    print("[+] Open Swagger Documentation in your browser: http://127.0.0.1:8000/docs\n")
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
