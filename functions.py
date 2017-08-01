# functions
from socket import *
import random

it = 0
userid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

protocol = {1: 'HELLO', 2: 'CONNECTED', 3: 'CHAT_REQUEST', 4: 'CHAT_STARTED', 5: 'UNREACHABLE', 6: 'END_REQUEST',
            7: 'END_NOTIF', 8: 'CHAT', 9: 'HIST_REQ', 10: 'HIST_RESP', 11: 'log out'}

testtest = {}
online = {}
serverName = gethostname()


def validate(x):
    "Checks to see if user has a valid id matching the ones on the list"
    isvalid = False
    if x in userid:
    #f idport.has_key(x):
        if x not in online:
            isValid = True
    return isValid

def get_chat_id():
    return random.randint(1000, 9999)

def go_online(x):  # needs validation
    online[x] = 0

def create_chat(x, y):
    chatid = get_chat_id()
    online[x] = chatid
    online[y] = chatid



# Nick's portion, open to editing
# # these variables are for testing purposes
# sessionID = 123
# nameOfClient = "Nick"
# loop = True


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
    # if not os.path.exists("logs"):
    #     os.makedirs("logs")
    #
    # createChatHistory(sessionID)

    # Here we have a loop for testing the functions.
    # The idea is this loop will run during chat, so we can record messages into a file,
    # then the user can call the history and we could cat the history file to the
    # user's screen.
    # print "Update the history!"
    # while loop:
    #
    #     message = raw_input()
    #     updateHistory(sessionID, sessionID, nameOfClient, message)
    #     if message == "00":
    #         loop = False





# def string_checker(str):
#     if protocol[3] in str:
#         #do the parsing
#     elif protocol[6] in str:
#         #do the parsing
#     elif protocol[]
#


# while 1:
#     localstring[self.iterator] = sockets[self.owner].recv(1024)
#
#     if protocol[3] in localstring[self.iterator]:
#         #gets user from CHAT_REQUEST-A-B
#         #checks if users are engaged in a chat already
#         #if so
#             #sockets[self.iterator].send(protocol[5]) '''unreachable
#         #ifnot
#             #create_chat(self.owner, destinationUser)
#             #send to both users that a chat has started (also sends session number)
#
#     elif protocol[6] in localstring[self.iterator]:
#         #gets the session ID from the END_REQUEST####
#         #modifies online['client1'] and online['client2' to 0
#         #send ENDNOTIF to both client1 and client2
#
#     elif protocol[8] in localstring[self.iterator]:
#         #checks to see if owner is in chat
#         #reads the four characters after CHAT to determine the session number
#         #uses chat session number to assign owner
#         #writes string to file
#         #sockets[destinationUser].send(localstring[self.iterator])
#
#     elif protocol[9] in localstring[self.iterator]:
#         #gets sessionid from HIST_REQclient1client2




str = 'CHAT_REQUEST-666'
#if protocol[1] or protocol[3] or protocol[6] or protocol[9] in str:
if any(x in str for x in protocol.values()):
    print "found one - do nothing"
else:
    print "append CHAT + ID"

str2 = int(str[13:16])
print str2



    #if localstring[self.iterator] == protocol[3]:
    #check to see if client is available
    #if client is available:
        # send a protocol[4]
        #while localstring[self.iterator] != protocol[6]:
        #localstring[self.iterator] = sockets[self.owner].recv(1024)  # receive line from client
        #sockets[destinationUser].send(localstring[self.iterator])
    #else



