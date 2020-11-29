from pathlib import Path
from cryptography.fernet import Fernet
from file_handler import write_data, read_data


def encrypt(data: bytes):
    create_key()
    key = Fernet(read_data(Path("key.key")))
    return key.encrypt(data)


def create_key():
    key = Fernet.generate_key()
    write_data(key.decode(), Path("key.key"))


def decrypt(data: bytes):
    key = Fernet(read_data(Path("key.key")))
    return key.decrypt(data)
