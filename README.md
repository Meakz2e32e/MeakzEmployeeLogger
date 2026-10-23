# EMPLOYEE LOGGER — README

**Author:** Meakz  
**Version:** 1.0  
**Created:** 22/10/2026  
**Language:** Python  
**Storage:** `employees.txt`

---

## WHAT IS IT?

Employee Logger is a Python terminal program I made to add employee records and search through them.

I built it as a personal project to practise Python and learn how to work with files, functions, user input and MAINLY searching for specific records within text documents.

## FEATURES

- add new employee records.
- search for employees using their Special ID Code or name.
- save employee information to a text file.
- give each employee an access level from 1 to 5.
- generate unique employee ID codes.
- confirm certain actions before carrying them out.

## EMPLOYEE RECORDS

Each employee record contains the following information:

| Name | Employee's full name |
| Department | Their department |
| Access Level | A number between 1 and 5 |
| Special ID Code | Their unique employee ID |

pretty cool if you ask me! :(

### Access Levels

Each employee is assigned an access level between `1` and `5`.

## SPECIAL ID CODE

Every employee gets a unique ID code.

Example:

- `00001`
- `00002`
- `00003`

The codes use five digits, with zeros at the beginning for 100,000 unique numbers aka users. .

## DATA STORAGE

Employee records are saved in `employees.txt`.

The file keeps the records saved when the program closes, so they can be accessed again next time.

Keep `employees.txt` in the location expected by the Python script.

## IMPORTS I USED

**`os`**

Used for clearing the terminal and checking whether files exist.

Documentation: https://docs.python.org/3/library/os.html

**`time`**

Just Used for adding delays between mesages and actions in the terminal tbh.

Documentation: https://docs.python.org/3/library/time.html

## LIMITATIONS

This is a personal Python project, not a proper employee management system.

The records are stored in a normal text file, so they arent encrypted or protected by proper access controls. Pls dont use it to store real confidential employee information.

## WHY I MADE IT

I wanted to build something that actually does something useful instead of just following tutorials. It gave me a chance to practise Python by making a program that can save, add and search for records.
