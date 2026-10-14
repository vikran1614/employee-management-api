from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.routes.employees import router as employees_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


@app.get("/")
def root():
    return {
        "message": f"{settings.app_name} is running",
        "docs": "/docs",
        "health": "/api/v1/health",
    }


app.include_router(health_router, prefix="/api/v1")
app.include_router(employees_router, prefix="/api/v1")
