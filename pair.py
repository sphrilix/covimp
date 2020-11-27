from participant import Participant


class Pair:
    imp: Participant

    receiver: Participant

    def __init__(self, imp: Participant, receiver: Participant):
        if imp == receiver or imp is None or receiver is None:
            raise ValueError("Imp and/or receiver are invalid")
        self.imp = imp
        self.receiver = receiver

    def __str__(self):
        return "###################################################################\n" \
            "Imp:\n{0} \n------------------------------------------------------------------- \nReceiver:\n{1}\n" \
               "###################################################################\n".format(self.imp, self.receiver)
