LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "101 North Nashville Dr"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "912 South Nashville Dr"
    }
]


def get_all_locations():
    return LOCATIONS

    # Function with a single parameter
def get_single_location(id):
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location

def create_location(location):
    # Get the id value of the last location in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    location["id"] = new_id

    # Add the location dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location

def delete_location(id):
    location_index = -1

    for index, location in enumerate(LOCATIONS):
        if location['id'] == id:                  # dictionaries use bracket notation, not dot notation
            location_index = index

    if location_index >= 0:
        LOCATIONS.pop(location_index)
