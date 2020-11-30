from pathlib import Path

from address import Address
from participant import Participant


# Returning the participants by reading the participants.txt line by line
def read_participants():
    participants = []
    raw_data = str(read_data(Path("participants.txt"))).strip("\n")
    raw_participants = raw_data.split("\n")
    for raw_participant in raw_participants:
        raw_participant = raw_participant.split(",")
        participants.append(Participant(raw_participant[0], raw_participant[1], Address(raw_participant[2],
                                                                                        raw_participant[3],
                                                                                        raw_participant[4],
                                                                                        raw_participant[5])))
    return participants


# Check if file existing
def is_file_existing(file: Path):
    return file.is_file()


# Write given data in a given file
def write_data(data: str, file: Path):
    if is_file_existing(file):
        with open(file, "w") as file:
            file.write(data)
    else:
        raise ValueError("Invalid file")


# Read a data from a given file
def read_data(file: Path):
    if is_file_existing(file):
        with open(file, "r") as file:
            return file.read()
    else:
        raise ValueError("Invalid file")


# Read data as bytes from a given file
def read_data_as_bytes(file: Path):
    if is_file_existing(file):
        with open(file, "rb") as file:
            return file.read()
    else:
        raise ValueError("Invalid file")


# Write given bytes to a given file
def write_data_as_bytes(data: bytes, file: Path):
    if is_file_existing(file):
        with open(file, "wb") as file:
            file.write(data)
    else:
        raise ValueError("Invalid file")