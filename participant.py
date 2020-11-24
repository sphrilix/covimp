from address import Address
import re


class Participant:
    MAIL_REG = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
    name: str

    mail: str

    address: Address

    def __init__(self, name: str, mail: str, address: Address):
        if not re.compile(self.MAIL_REG).fullmatch(mail):
            raise ValueError("Invalid Mail")
        if name is None or address is None:
            raise ValueError("A or more params cannot be null")
        self.name = name
        self.mail = mail
        self.address = address

    def __str__(self):
        return "{0},{1},{2}".format(self.name, self.mail, self.address)


p = Participant("m", "msdadadad@ndadadadada.de", Address("94051", "H", "s", "10"))
print(p)
print(p)