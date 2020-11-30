import re

from address import Address


# Simple data container for a participant
class Participant:

    # Regex for mail
    MAIL_REG = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"

    # Name of the participant
    name: str

    # Mail of the participant
    mail: str

    # Address of the participant
    address: Address

    # Create a new instance of a participant with the given params
    def __init__(self, name: str, mail: str, address: Address):
        if not re.compile(self.MAIL_REG).fullmatch(mail):
            raise ValueError("Invalid Mail")
        if name is None or address is None:
            raise ValueError("A or more params cannot be null")
        self.name = name
        self.mail = mail
        self.address = address

    # Returning a textual representation of a participant
    def __str__(self):
        return "Name: {0} \nMail: {1} \nAddress: {2}".format(self.name, self.mail, self.address)

    # Returning if two participants are equal by comparing the name
    def __eq__(self, other):
        return self.name == other.name
