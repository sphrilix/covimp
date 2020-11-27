from participant import Participant
from address import Address
from pair import Pair
from random import randint
from file_handler import read_participants
from  file_handler import write_data


def main():
    pairs = create_random_pairs()
    write_data(pairs)


def create_random_pairs():
    random_pairs = None
    while random_pairs is None:
        random_pairs = create_random_pairs_help(read_participants())
    return random_pairs


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


if __name__ == '__main__':
    main()
