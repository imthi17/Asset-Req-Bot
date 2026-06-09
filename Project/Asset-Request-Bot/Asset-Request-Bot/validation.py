import json

HRIS_FILE = "hris/employees.json"


def load_employees():
    try:
        with open(HRIS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def get_employee(employee_id):
    employees = load_employees()

    for employee in employees:
        if employee["employee_id"].upper() == employee_id.upper():
            return employee

    return None


def validate_employee(employee_id):
    employee = get_employee(employee_id)

    if employee:
        return True, employee

    return False, None


def is_asset_allowed(employee, asset_type):
    role = employee.get("role", "")
    grade = employee.get("grade", "")

    # Example business rules
    if asset_type.lower() == "macbook":
        return grade in ["G5", "G6", "G7"]

    if asset_type.lower() == "premium laptop":
        return grade in ["G5", "G6", "G7"]

    if employee["role"] == "Intern" and asset_type.lower() == "macbook":
        return False

    return True


if __name__ == "__main__":
    valid, employee = validate_employee("EMP1001")

    if valid:
        print("Employee Found")
        print(employee)
    else:
        print("Employee Not Found")