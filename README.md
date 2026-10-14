## Task 4 — Master Dataset and Seed Pipeline

### Overview

This project provides a generated HR master dataset for employee management, salary processing, attendance tracking, analytics, and reporting.

### Generated files

| File | Description |
|---|---|
| `sample_data/employees_master.csv` | Master employee dataset (50 records) |
| `sample_data/employees_master.json` | Employee data in JSON format (50 records) |
| `sample_data/salaries.csv` | Salary records linked to employees (50 records) |
| `sample_data/attendance.csv` | Attendance records linked to employees (1,100 records) |

### Generate the datasets

With Docker Compose running, execute:

```powershell
docker compose exec api python scripts/generate_master_dataset.py
```

### Verify the API tests

```powershell
docker compose exec api python -m pytest -v
```

### Data integrity

The generated datasets have been checked for matching employee IDs between the employee and salary files, valid employee references in attendance, and duplicate employee IDs in the master dataset.

### Notes

These datasets are generated sample data for development and testing. They are not production employee records.