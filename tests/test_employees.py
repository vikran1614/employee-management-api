
from datetime import date

from fastapi.testclient import TestClient

from app.db.dependencies import get_db
from app.main import app
from app.models import Department, Employee, Role


def test_list_employees_endpoint_is_available():
    response = TestClient(app).get("/api/v1/employees/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_nonexistent_employee_returns_404():
    response = TestClient(app).get("/api/v1/employees/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"


def test_delete_nonexistent_employee_returns_404():
    response = TestClient(app).delete("/api/v1/employees/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"
