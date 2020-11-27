from pathlib import Path

from cryptography.fernet import Fernet
from datetime import date
from file_handler import write_data, read_data


def encrypt(data: str):
    create_key()
    key = Fernet(read_data(Path("key.key")))
    data = data.encode()
    return key.encrypt(data)


def create_key():
    key = Fernet.generate_key()
    write_data(Path("key.key"), key)


def decrypt(data: str):
