import re


# Simple data container for a address
class Address:

    # Regex for postal code
    POSTAL_REG = r"\d\d\d\d\d"

    # Postal code of the address
    postal_code: str

    # City of the address
    city: str

    # Street of the address
    street: str

    # House number of the address
    house_number: str

    # Constructing new address with given params
    def __init__(self, postal_code: str, city: str, street: str, house_number: str):
        if not re.compile(self.POSTAL_REG).fullmatch(postal_code):
            raise ValueError("Illegal postal code!")
        elif city is None or street is None or house_number is None:
            raise ValueError("One or more params can't be null!")
        self.postal_code = postal_code
        self.city = city
        self.street = street
        self.house_number = house_number

    # Return a textual representation of an address
    def __str__(self):
        return "{0} {1}, {2} {3}".format(self.postal_code, self.city, self.street, self.house_number)
