#functions
from socket import *
import os

it = 0
userid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
sPorts = [12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020]
serverName = gethostname()

def validate (x):
    "Checks to see if user has a valid id matching the ones on the list"
    isvalid = False
    for y in range (0, 9):
        if (x == userid[y]):
            isvalid = True
        else:
            continue
    return isvalid

def get_sport():
    if len(sPorts) == 0:
        return 'no port available'
    else:
        portNo = sPorts[0]
        del sPorts[0]
        return portNo

# for it in range (12010, 12022):
#     try:
#         print sPorts.index(it)
#     except ValueError:
#         print "not found"




# Nick's portion, open to editing
# these variables are for testing purposes
sessionID = 123
nameOfClient = "Nick"
loop = True


def createChatHistory(sessionID):
    # makes a file that goes into the logs folder
    f = open("logs/" + str(sessionID), "w+")

    # write a line to the file
    f.write("<session_id>\t<from: sending client>\t<chat message> **00 indicates end of history** \n")

    f.close()


# where history is the history file, ex '1234.txt'
def updateHistory(history, sessionID, nameOfClient, message):
    # now we're going to append the file
    f = open("logs/" + str(history), "a+")

    f.write(str(sessionID) + "\t\t" + str(nameOfClient) + "\t\t" + str(message) + "\n")

    f.close()

# Is there a logs folder? If not, create one
if not os.path.exists("logs"):
    os.makedirs("logs")

createChatHistory(sessionID)

# Here we have a loop for testing the functions.
# The idea is this loop will run during chat, so we can record messages into a file,
# then the user can call the history and we could cat the history file to the
# user's screen.
print "Update the history!"
while loop:

    message = raw_input()
    updateHistory(sessionID, sessionID, nameOfClient, message)
    if message == "00":
        loop = False
