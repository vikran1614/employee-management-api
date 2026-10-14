
import csv
import json
import random
from datetime import date, timedelta
from pathlib import Path

from faker import Faker

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "sample_data"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DEPARTMENTS = {
    "Engineering": ["Software Engineer", "Backend Developer"],
    "Data": ["Data Analyst", "Data Engineer"],
    "HR": ["HR Executive", "Recruiter"],
    "Finance": ["Accountant", "Payroll Analyst"],
}


def generate_dataset(employee_count=50):
    employees = []
    salaries = []
    attendance = []
    start_date = date.today() - timedelta(days=30)

    for employee_id in range(1, employee_count + 1):
        first_name = fake.first_name()
        last_name = fake.last_name()
        department = random.choice(list(DEPARTMENTS))
        role = random.choice(DEPARTMENTS[department])

        employees.append({
            "employee_id": employee_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": f"employee{employee_id}@example.com",
            "department": department,
            "role": role,
            "hire_date": fake.date_between(
                start_date="-5y", end_date="today"
            ).isoformat(),
            "status": random.choice(
                ["active", "active", "active", "inactive"]
            ),
        })

        salaries.append({
            "employee_id": employee_id,
            "monthly_salary_inr": random.randrange(25000, 100001, 1000),
            "currency": "INR",
            "effective_date": date.today().isoformat(),
        })

        for day_offset in range(30):
            attendance_date = start_date + timedelta(days=day_offset)

            if attendance_date.weekday() >= 5:
                continue

            attendance_status = random.choices(
                ["present", "absent", "leave"],
                weights=[90, 5, 5],
                k=1,
            )[0]

            attendance.append({
                "employee_id": employee_id,
                "attendance_date": attendance_date.isoformat(),
                "status": attendance_status,
            })

    return employees, salaries, attendance


def write_csv(filename, rows):
    path = OUTPUT_DIR / filename

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"Created {path.relative_to(ROOT)} ({len(rows)} rows)")


def main():
    employees, salaries, attendance = generate_dataset()

    write_csv("employees_master.csv", employees)
    write_csv("salaries.csv", salaries)
    write_csv("attendance.csv", attendance)

    json_path = OUTPUT_DIR / "employees_master.json"
    with json_path.open("w", encoding="utf-8") as file:
        json.dump(employees, file, indent=2)

    print(f"Created {json_path.relative_to(ROOT)} ({len(employees)} records)")
    print("Master dataset generation completed successfully.")


if __name__ == "__main__":
    main()
