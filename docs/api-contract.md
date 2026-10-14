# Employee Management API — Draft Contract

Base URL: /api/v1

## Health Check

GET /api/v1/health

Success response — 200 OK

{
  "status": "ok",
  "service": "employee-management-api",
  "version": "0.1.0"
}

## Employees (planned)

POST /api/v1/employees
Create an employee. Expected response: 201 Created.

GET /api/v1/employees
List employees. Supports pagination, filtering, and search.

GET /api/v1/employees/{employee_id}
Retrieve one employee. Expected response: 200 OK.

PATCH /api/v1/employees/{employee_id}
Update an employee. Expected response: 200 OK.

DELETE /api/v1/employees/{employee_id}
Delete an employee. Expected response: 204 No Content.

## Error Responses

Use standard HTTP status codes and a consistent JSON error structure.
Detailed validation, pagination, and error formats remain to be confirmed
against the project guide before implementation.
