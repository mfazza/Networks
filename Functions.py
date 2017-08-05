# functions.py
#Created by Mathews Fazza and Nickolas Ramos
#
#This file contains the functions used by all programs in the client-server architecture project
#Functions are invoked as necessary.  Nothing needs to be done in order to run this program


from socket import *
import random
import os

it = 0                                                          #simple iterator
userid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']     #list of user ids


#dictionary of protocols
protocol = {1: 'HELLO', 2: 'CONNECTED', 3: 'CHAT_REQUEST', 4: 'CHAT_STARTED', 5: 'UNREACHABLE', 6: 'END_REQUEST',
            7: 'END_NOTIF', 8: 'TALK', 9: 'HISTORY_REQ', 10: 'HISTORY_RESP', 11: 'log out', 12: 'SNUM', 13: 'HELP'}

online = {}                                                     #dictionary of users online
serverName = gethostname()                                      #name of server


def validate(x):                                                #Checks to see if user has a valid id matching userid[]
    isValid = False
    if x in userid:
        if x not in online:
            isValid = True
    return isValid

def get_chat_id():                                              #returns a random chat id number from 1000 to 9999
    return random.randint(1000, 9999)

def go_online(x):                                               #inserts 'x: 0' into online{}
    online[x] = 0

def create_chat(x, y):                                          #creating a chat, means setting the number in
    chatid = get_chat_id()                                      #online{} from 0 to a random returned by the function
    online[x] = chatid
    online[y] = chatid                                          #both users involved in the same chat get the same number



def createChatHistory(sender, receiver, sessionID, nameOfClient, message):  #checks to see if a folder exists, if the files exist,
                                                                            #and furthermore, creates or appends files with messages.
    if os.path.exists("logs") == False:
        os.makedirs("logs")

    # If the file doesn't exist, makes a file that goes into the logs folder
    if not os.path.exists(str(sender) + "-" + str(receiver)):
        f = open("logs/" + str(sender) + "-" + str(receiver), "a+")

    # write a line to the file
    if os.path.exists("logs/" + str(sender) + "-" + str(receiver)):
        f.write("<" + str(sessionID) + ">" + "\t" + "<" + str(nameOfClient) + ">" + "\t" + str(message) + "\n")

    f.close()

#gethelp function is just a way to aid users in typing the commands
def gethelp():
    print "Each command can be typed at any moment.  Commands should be typed in caps lock using the following format: COMMAND(arguments).\n"
    print "CHAT_REQUEST(a-b) where a and b are users and should be lower case separated by a dash\n"
    print"END_REQUEST(####) where #### is the four digit numebr identifying the chat session number\n"
    print "HISTORY_REQUEST(a-b) where a and b are users and should be lower case separated by a dash\n"
    print "SNUM displays the number of current chat session if there is one.  The number 77 indicates there is no session\n"
    print "log out   log out, typed in lower case, separated by a space, disconnects the user from the server"




