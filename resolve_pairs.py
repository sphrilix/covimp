from datetime import date
from pathlib import Path

from encryption import decrypt
from file_handler import read_data_as_bytes, write_data

DAY_OF_RESOLVE = 25
MONTH_OF_RESOLVE = 12


def main():
    print(get_pairs())


def get_pairs():
    if DAY_OF_RESOLVE <= date.today().day and MONTH_OF_RESOLVE <= date.today().month:
        pairs = (decrypt(read_data_as_bytes(Path("pairs.txt")))).decode()
        write_data(pairs, Path("pairs.txt"))
        return pairs
    else:
        return "Too early wait until release"


if __name__ == '__main__':
    main()