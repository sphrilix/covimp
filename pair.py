from participant import Participant


# Simple data container for a imp, receiver pairing
class Pair:

    # Imp of the pairing
    imp: Participant

    # Receiver of the pairing
    receiver: Participant

    # Create a new pairing with given imp and receiver
    def __init__(self, imp: Participant, receiver: Participant):
        if imp == receiver or imp is None or receiver is None:
            raise ValueError("Imp and/or receiver are invalid")
        self.imp = imp
        self.receiver = receiver

    # Return a textual representation of a pairing
    def __str__(self):
        return "###################################################################\n" \
            "Imp:\n{0} \n------------------------------------------------------------------- \nReceiver:\n{1}\n" \
               "###################################################################\n".format(self.imp, self.receiver)
