
from sqlalchemy.orm import configure_mappers

from app.db.base import Base
from app.models import Department, Employee, Role


def test_all_tables_are_registered():
    assert set(Base.metadata.tables.keys()) == {
        "departments",
        "employees",
        "roles",
    }


def test_model_relationships_are_configured():
    configure_mappers()

    assert hasattr(Department, "employees")
    assert hasattr(Department, "roles")
    assert hasattr(Role, "department")
    assert hasattr(Role, "employees")
    assert hasattr(Employee, "department")
    assert hasattr(Employee, "role")
    assert hasattr(Employee, "manager")
    assert hasattr(Employee, "team_members")
