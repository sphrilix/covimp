from pathlib import Path
import pyinputplus as pyinp
from create_pairs import create_random_pairs
from file_handler import read_data
from mail_handler import send_mails
from resolve_pairs import resolve_pairs


# Handling the user input
def main():
    end = False
    while end is False:
        if read_data(Path("pairs.txt")) == "":
            print("Hello there,\nThank you for using covimp! \nMake sure you entered the correct data to the files. "
                  "\nParticipants in the participants.txt with the following syntax: name,mail,postal code,city,street,"
                  "house number! \nMail account data in config.txt with the following syntax: smtp_server,port,mail,"
                  "password!\nIf so you can start creating pairs! Do you want to create them?")
            if pyinp.inputYesNo() == "yes":
                subject = pyinp.inputStr("Enter the subject of the mail to be sent: ")
                salutations = pyinp.inputStr("Enter the salutations: ")
                message_body = pyinp.inputStr("Enter the message body: ")
                greetings = pyinp.inputStr("Enter greetings: ")
                send_mails(create_random_pairs(), subject, salutations, message_body, greetings)
                print("Mails were sent. Merry Christmas!")
                end = True
            else:
                print("Merry chirstmas and a happy new year!")
                end = True
        else:
            print("Hello, \nYou already created pairs. Do you want to resolve them?")
            if pyinp.inputYesNo() == "yes":
                print(resolve_pairs())
                print("I hope you enjoyed using covimp! Give a star on github :)! Merry christmas and a happy new "
                      "year!")
                end = True
            else:
                print("Merry christmas and a happy new year!")
                end = True


# Entry point of the application
if __name__ == '__main__':
    main()
