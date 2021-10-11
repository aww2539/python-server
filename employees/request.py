EMPLOYEES = [
    {
        "id": 1,
        "name": "Luke Skywalker",
        "address": "333 Degoba System",
        "location_id": 1
    },
    {
        "id": 2,
        "name": "Bart Simpson",
        "address": "90 Cartoon Way",
        "location_id": 1
    },
    {
        "id": 3,
        "name": "Harry Potter",
        "address": "588 Hogwarts Stuff",
        "location_id": 2
    },
    {
        "id": 4,
        "name": "Frodo Baggins",
        "address": "102 Somewhere in the shire blvd",
        "location_id": 2
    }
]

def get_all_employees():
    return EMPLOYEES

    # Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the employeeS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
