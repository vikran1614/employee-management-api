
from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class EmployeeBase(BaseModel):
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    hire_date: date
    status: str = Field(default="active", max_length=30)
    department_id: int = Field(gt=0)
    role_id: int = Field(gt=0)
    manager_id: int | None = Field(default=None, gt=0)


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    first_name: str | None = Field(default=None, min_length=1, max_length=100)
    last_name: str | None = Field(default=None, min_length=1, max_length=100)
    email: EmailStr | None = None
    hire_date: date | None = None
    status: str | None = Field(default=None, max_length=30)
    department_id: int | None = Field(default=None, gt=0)
    role_id: int | None = Field(default=None, gt=0)
    manager_id: int | None = Field(default=None, gt=0)


class EmployeeResponse(EmployeeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
