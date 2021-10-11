CUSTOMERS = [
    {
        "id": 1,
        "name": "Santa Clasue",
        "address": "2076 N Pole Blvd",
        "email": "hollyjolly@clause.com",
        "password": "gifts"
    },
    {
        "id": 2,
        "name": "Mr. President",
        "address": "1600 Penn Ave",
        "email": "theone@gov.gov",
        "password": "idk"
    },
    {
        "id": 3,
        "name": "Marry Poppins",
        "address": "1 is the Lonliest Ave",
        "email": "letsfly@imagine.com",
        "password": "raindrops"
    },
    {
        "id": 4,
        "name": "Boba Fett",
        "address": "111 Camino Station",
        "email": "thehunter@bounty.com",
        "password": "blaster"
    }
]

def get_all_customers():
    return CUSTOMERS

    # Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the customerS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer