from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy import or_, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models import Department, Employee, Role
from app.schemas.employee import EmployeeCreate, EmployeeResponse, EmployeeUpdate

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(
    employee_data: EmployeeCreate,
    db: Session = Depends(get_db),
):
    department = db.get(Department, employee_data.department_id)
    role = db.get(Role, employee_data.role_id)

    if department is None:
        raise HTTPException(status_code=404, detail="Department not found")

    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")

    if role.department_id != employee_data.department_id:
        raise HTTPException(
            status_code=400,
            detail="Role does not belong to the selected department",
        )

    if employee_data.manager_id is not None:
        if db.get(Employee, employee_data.manager_id) is None:
            raise HTTPException(status_code=404, detail="Manager not found")

    employee = Employee(**employee_data.model_dump())
    db.add(employee)

    try:
        db.commit()
        db.refresh(employee)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Employee could not be created; check for a duplicate email or invalid relationship",
        )

    return employee


@router.get("/", response_model=list[EmployeeResponse])
def list_employees(
    page: int = Query(default=1, ge=1),
    size: int = Query(default=10, ge=1, le=100),
    department_id: int | None = Query(default=None, gt=0),
    status_filter: str | None = Query(default=None, alias="status"),
    search: str | None = Query(default=None, min_length=1, max_length=100),
    db: Session = Depends(get_db),
):
    statement = select(Employee)

    if department_id is not None:
        statement = statement.where(Employee.department_id == department_id)

    if status_filter is not None:
        statement = statement.where(Employee.status == status_filter)

    if search:
        term = f"%{search.strip()}%"
        statement = statement.where(
            or_(
                Employee.first_name.ilike(term),
                Employee.last_name.ilike(term),
                Employee.email.ilike(term),
            )
        )

    statement = statement.order_by(Employee.id).offset((page - 1) * size).limit(size)
    return db.scalars(statement).all()


@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db),
):
    employee = db.get(Employee, employee_id)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


@router.patch("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    employee_data: EmployeeUpdate,
    db: Session = Depends(get_db),
):
    employee = db.get(Employee, employee_id)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    changes = employee_data.model_dump(exclude_unset=True)

    for field, value in changes.items():
        if value is None and field != "manager_id":
            raise HTTPException(
                status_code=422,
                detail=f"{field} cannot be null",
            )

    department_id = changes.get("department_id", employee.department_id)
    role_id = changes.get("role_id", employee.role_id)
    manager_id = changes.get("manager_id", employee.manager_id)

    if db.get(Department, department_id) is None:
        raise HTTPException(status_code=404, detail="Department not found")

    role = db.get(Role, role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")

    if role.department_id != department_id:
        raise HTTPException(
            status_code=400,
            detail="Role does not belong to the selected department",
        )

    if manager_id == employee.id:
        raise HTTPException(status_code=400, detail="An employee cannot manage themselves")

    if manager_id is not None and db.get(Employee, manager_id) is None:
        raise HTTPException(status_code=404, detail="Manager not found")

    for field, value in changes.items():
        setattr(employee, field, value)

    try:
        db.commit()
        db.refresh(employee)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Update conflicts with existing data")

    return employee


@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db),
):
    employee = db.get(Employee, employee_id)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(employee)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Employee cannot be deleted because other records depend on it",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
