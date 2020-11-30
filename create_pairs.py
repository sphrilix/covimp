from pathlib import Path
from random import randint

from encryption import encrypt
from file_handler import read_participants, write_data_as_bytes
from pair import Pair


# Return the random created pairs and writing them encrypted in pairs.txt
def create_random_pairs():
    random_pairs = None
    while random_pairs is None:
        random_pairs = create_random_pairs_help(read_participants())
    pairs_str = ""
    for pair in random_pairs:
        pairs_str += str(pair)
    encrypted_pairs = encrypt(pairs_str.encode())
    write_data_as_bytes(encrypted_pairs, Path("pairs.txt"))
    return random_pairs


# Try to create pairs if it doesn't work return None, else return created pairs.
def create_random_pairs_help(participants: []):
    not_yet_receiver = participants.copy()
    pairs = []
    for imp in participants:
        receiver = not_yet_receiver[randint(0, len(not_yet_receiver) - 1)]
        try:
            pairs.append(Pair(imp, receiver))
        except ValueError:
            return None
        not_yet_receiver.remove(receiver)
    return pairs


