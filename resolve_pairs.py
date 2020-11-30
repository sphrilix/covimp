from datetime import date
from pathlib import Path

from encryption import decrypt
from file_handler import read_data_as_bytes, write_data

# Date on which the pairs should be released
DAY_OF_RESOLVE = 25
MONTH_OF_RESOLVE = 12
YEAR_OF_RESOLVE = 2020


# Return a textual representation of the pairs if it should be resolved, else return a error message. It also decrypts
# the pairs.txt.
def resolve_pairs():
    if (DAY_OF_RESOLVE <= date.today().day and MONTH_OF_RESOLVE <= date.today().month) or \
            date.today().year > YEAR_OF_RESOLVE:
        pairs = (decrypt(read_data_as_bytes(Path("pairs.txt")))).decode()
        write_data(pairs, Path("pairs.txt"))
        return pairs
    else:
        return "Too early wait until release date!"
