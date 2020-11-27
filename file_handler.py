from pair import Pair
from participant import Participant
from address import Address


def read_participants():
    participants = []
    with open("participants.txt", "r") as file:
        for line in file.readlines():
            line.strip(" ")
            raw_data = line.split(",")
            participants.append(Participant(raw_data[0], raw_data[1], Address(raw_data[2], raw_data[3], raw_data[4],
                                                                              raw_data[5])))
        return participants


def write_data(pairs: []):
    with open("pairs.txt", "w") as file:
        for p in pairs:
            if isinstance(p, Pair):
                file.write(str(p))

'''
p = Participant("m", "msdadadad@ndadadadada.de", Address("94051", "H", "s", "10"))
participants = [p, p]
write_data(participants)
p2 = read_participants()
for p in p2:
    print(p)
'''