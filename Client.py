#Client.py
#Created by Mathews Fazza and Nickolas Ramos
#
#This is the client that connects to server.py.  For detailed instructions on how to run the program, please refer to the
#program report.  Run the program, choose a username, and type 'log on' in order to run the program.


from socket import *
from Feistel import *
import time
import threading
from Functions import *
import string



menu1 = 'sdkljfhds'                                     #variable for the first menu
user_Id = '9'                                           #user id
#serverName = gethostname()                             #gets the name of the host (which is interface dependent)
serverName = gethostbyname("localhost")
serverPort = 12000                                      #hard coded port
receivedPort = 0

# Security Addition
# eKey = random.choice(string.letters)
# print eKey
eKey = "z"


#protocol = {1: 'HELLO', 2: 'CONNECTED', 3: 'CHAT_REQUEST', 4: 'CHAT_STARTED', 5: 'UNREACHABLE', 6: 'END_REQUEST',
 #           7: 'END_NOTIF', 8: 'TALK', 9: 'HISTORY_REQ', 10: 'HISTORY_RESP', 11: 'log out', 12: 'SNUM', 13: 'HELP'}

class receiving(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global currentChat
        currentChat = 77
        #while powerbutton:
        while 1:
            if powerbutton == False:
                break

            output = clientSocket.recv(1024)

            if protocol[5] in output:
                print "Correspondent unreachable"
            elif protocol[4] in output:
                currentChat = output[13:17]
                print "Chat started"
            elif protocol[7] in output:
                currentChat = 77
                print "Chat ended"
            elif protocol[11] in output:
                self._Thread__stop()
            else:
                decrypt = feistelAtWork(output, eKey, "d")
                print "CHAT: " + decrypt


class sending(threading.Thread):                        #overrides threading.Thread's __init__ and run functions
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        global powerbutton                              #powerbutton turns the threads off when needed
        powerbutton = True

        while 1:

            togo = raw_input() #368911                  #gets input from user

            if protocol[3] in togo:                     #if CHAT_REQUEST is a substring of what the user typed
                if togo[12] == "(" and togo[16] == ")": #validate it
                    clientSocket.send(togo)             #then send it to the server
            elif protocol[6] in togo:                   #if END_REQUEST is a substring of what the user typed
                if togo[12:16] == currentChat:
                    clientSocket.send(togo)
            elif protocol[8] in togo:                   #if TALK is a substring of what the user typed
                eMessage = feistelAtWork(togo, eKey, "e")
                clientSocket.send(protocol[8] + "(" + str(currentChat) + ")" + eMessage )
            elif protocol[9] in togo:                   #if HISTORY_REQ is a substring of what the user typed
                clientSocket.send(togo)
            elif protocol[11] in togo:                  #if user types 'log out'
                print "Disconnected"                    #displays 'Disconnected'
                clientSocket.send(togo)                 #sends 'log out' to server
                clientSocket.close()                    #closes socket
                powerbutton = False                     #turns of threads in the client process
                self._Thread__stop()
                break
            elif protocol[12] in togo:                  #if SNUM is a substring of what the user typed
                print "Current chat session ID: " + currentChat #returns the chat id number
            elif protocol[13] in togo:                  #if user types 'HELP' displays the HELP message
                gethelp()
            else:
                if currentChat != 77:                   #all other cases + user in chat, sends string to server
                    eMessage = feistelAtWork(togo, eKey, "e")
                    clientSocket.send(protocol[8] + "(" + str(currentChat) + ")" + eMessage)





while user_Id.isalpha() == False or user_Id.islower() == False: #gets id from user
    user_Id = raw_input("Please enter your user ID (unique lower case letter):\n")


while menu1 not in ['log on', 'log out']:                       #logs user in
    menu1 = raw_input("Please enter 'log on' to connect to the server or 'disconnect' to leave.\n")

if menu1 == "log out":
    exit()

HELLO = user_Id                                         #used this to make it more relatable to the project guideline
clientSocket = socket(AF_INET, SOCK_STREAM)             #creates socket
clientSocket.connect((serverName, serverPort))          #connects to server's socket
clientSocket.send(HELLO)                                #validates server
confirmation = clientSocket.recv(1024)                  #receives confirmation from server
if confirmation != "CONNECTED":
    print "Declined"
    clientSocket.close()
    exit()

#at this point the server will receive the port for the chatsocket
print "server: Connected"

time.sleep(1)                                           #again, it only works after a slight delay

tosend = sending()
tosend.start()                                          #starts sending thread
toreceive = receiving()
toreceive.start()                                       #starts receiving thread