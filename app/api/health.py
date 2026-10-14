from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "employee-management-api",
        "version": "0.1.0",
    }
