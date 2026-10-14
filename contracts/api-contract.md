Employee Management API - Draft API Contract

Base URL:
http://localhost:8000

Health Check:
Method: GET
Endpoint: /api/v1/health
Purpose: Check whether the API is running.
Success status: 200 OK

Example response:
{
  "status": "ok",
  "service": "employee-management-api",
  "version": "0.1.0"
}

Planned Employee APIs:
POST /api/v1/employees - Create an employee
GET /api/v1/employees - List employees
GET /api/v1/employees/{employee_id} - Get employee details
PATCH /api/v1/employees/{employee_id} - Update employee details
DELETE /api/v1/employees/{employee_id} - Delete an employee

Note:
The employee APIs listed above are planned for future implementation.