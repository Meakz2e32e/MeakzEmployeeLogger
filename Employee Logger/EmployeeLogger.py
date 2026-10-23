## ==========================================
## Project: Employee Logger
## Author: Meakz
## Purpose: Record and Research employee information.
## ------------------------------------------
## Employee Fields:
## Name: {NAME}
## Department: {DEPARTMENT}
## Access_Level: {1-5}
## Special_Code: {EMPLOYEE_ID}
## ------------------------------------------
## Version: 1.0
## Created: 22/10/2026
## ==========================================

import os
import time

def carry_on():
    print("Are You Sure? (y/n)")
    carryonquestion = input(">> ").strip().lower()

    if carryonquestion == "y":
        return True
    elif carryonquestion == "n":
        print("Cancelled!")
        return False
    else:
        print("Invalid input!")
        return False


def add_member():
    print("Name of Employee? (e.g. James)")
    name_of_employee = input(">> ").strip().lower()

    print("Department? (e.g. Legal)")
    department_of_employment = input(">> ").strip().lower()

    print("Access level? (1-5)")
    access_level = input(">> ").strip()

    if access_level not in ["1", "2", "3", "4", "5"]:
        print("Invalid access level!")
        return

    last_id = 0

    if os.path.exists("employees.txt"):
        with open("employees.txt", "r") as file:
            for line in file:
                if line.startswith("Special ID Code: "):
                    try:
                        current_id = int(line.split(": ", 1)[1].strip())
                        last_id = max(last_id, current_id)
                    except ValueError:
                        pass

    special_code = f"{last_id + 1:05d}"

    print(f"Last Special ID Code was {last_id:05d}")
    print(f"New ID will be: {special_code}")

    with open("employees.txt", "a") as file:
        file.write(
            f"\n========== EMPLOYEE RECORD ==========\n"
            f"Name: {name_of_employee}\n"
            f"Department: {department_of_employment}\n"
            f"Access Level: {access_level}\n"
            f"Special ID Code: {special_code}\n"
            f"=====================================\n"
        )

    print("Employee added!")
    time.sleep(4)


def search_database():
    if not os.path.exists("employees.txt"):
        print("No employee records found!")
        return

    search_id = input("Enter Employee name or ID >> ").strip()

    with open("employees.txt", "r") as file:
        employees = file.read()

    records = employees.split("========== EMPLOYEE RECORD ==========")

    for record in records:
        if f"Special ID Code: {search_id}" in record or f"Name: {search_id}" in record:
            print("\n========== EMPLOYEE RECORD ==========")
            print(record.strip().split("=====================================")[0])
            print("=====================================")
            return

    print("Employee name or ID not found.")


def Question():
    while True:
        print("\n========== EMPLOYEE LOGGER ==========")
        print("1. ADD MEMBER")
        print("2. SEARCH FOR MEMBER")
        print("3. EXIT")

        choice_of_question = input(">> ").strip()

        if choice_of_question == "1":
            add_member()

        elif choice_of_question == "2":
            search_database()

        elif choice_of_question == "3":
            print("Closing Employee Logger...")
            time.sleep(1)
            break

        else:
            print("Invalid input. Please try again.")
            time.sleep(2)

        os.system("cls")


print("Loading Database...")
time.sleep(1)
print("Database Loaded!")
time.sleep(1)
os.system("cls")

Question()