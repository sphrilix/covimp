import re


class Address:
    POSTAL_REG = r"\d\d\d\d\d"
    postal_code: str
    city: str
    street: str
    house_number: str

    def __init__(self, postal_code: str, city: str, street: str, house_number: str):
        if not re.compile(self.POSTAL_REG).fullmatch(postal_code):
            raise ValueError("Illegal postal code!")
        elif city is None or street is None or house_number is None:
            raise ValueError("One or more params can't be null!")
        self.postal_code = postal_code
        self.city = city
        self.street = street
        self.house_number = house_number

    def __str__(self):
        return "{0} {1}, {2} {3}".format(self.postal_code, self.city, self.street, self.house_number)
