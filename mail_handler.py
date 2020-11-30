import smtplib
import ssl
from pathlib import Path

from address import Address
from file_handler import read_data
from pair import Pair
from participant import Participant

# Standard template for the message used in the mails
message_template = "Subject: {0}\n\n{1}\n{2}\n{3}\n\n----------------------------------------------------------------\n" \
                   "This mail was sent using covimp. Check https://github.com/sphrilix/covimp for further information"


# Notify everyone over mail
def send_mails(pairs: [], subject: str, message_body: str, greetings: str):
    raw_data = read_data(Path("config.txt")).strip("\n")
    smtp_server = raw_data.split(",")[0]
    port = raw_data.split(",")[1]
    sender_mail = raw_data.split(",")[2]
    password = raw_data.split(",")[3]
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_mail, password)
        for pair in pairs:
            message = message_template.format(subject, message_body, str(pair.receiver), greetings)
            server.sendmail(sender_mail, pair.receiver.mail, message)


if __name__ == '__main__':
    send_mails([Pair(Participant("Hi", "a@b.de", Address("94051", "s", "d", "12")), Participant("i",
                                                "maxi.jungwirth@gmail.com", Address("94051", "s", "d", "12")))], "Wichteln bei den Jungwirths", "Servus,\nDu darfst beschenken:\n", "Frohe WEihnachten")
