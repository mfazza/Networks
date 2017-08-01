from socket import *
from functions import *
import thread
import time
import threading

localstring = []                                            #array of string that is used by each thread
sessions = []                                               #array of individual threads (one per client)
count = 0                                                   #simple iterator.



#creates hashmap of sockets
users = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
sockets = {}
for x in range (0, 9):
    sockets[users[x]] = socket(AF_INET, SOCK_STREAM)

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)                 #creates socket and on the next line, binds it to a port
serverSocket.bind(('', serverPort))                         #leaving the first member of the tuple as '' denotes the welcoming socket
serverSocket.listen(1)                                      #ready to receive data from client
print "The server is ready to receive"


class BackgroundTask(threading.Thread):

    def __init__(self, i):
        threading.Thread.__init__(self)
        self.i = i


    def run(self):
        while 1:
            conn, addr = serverSocket.accept()  # Will indefinitely accept data from clients
            newuser = conn.recv(1024)           # receive (buffer size of 1024 bytes)
            validation = validate(newuser)      # It checks the userID for validation
            sockets[newuser] = conn             #passes object to dictionary 'a': socket

            # validation part
            if validation == True:  #if user connects successfully they receive a port number and new thread is created


                conn.send(protocol[2])
                print 'User ' + newuser + " has connected to the server"

                go_online(newuser)

                sessions.append(IndividualTask(newuser, self.i))
                sessions[self.i].start()

                print threading.enumerate()

                self.i += 1  # updates count

            else:
                conn.send("DECLINED\n")

class IndividualTask(threading.Thread):
    def __init__(self, owner, iterator):
        threading.Thread.__init__(self)
        self.iterator = iterator
        self.owner = owner

    def run(self):

        localstring.append('flks;ddksj')

        while 1:
            destinationUser = 'z'

            localstring[self.iterator] = sockets[self.owner].recv(1024)                        #receive line from client
            destinationUser = localstring[self.iterator]

            if destinationUser in online.keys() and online[self.owner] == 0 and online[destinationUser] == 0:
                create_chat(self.owner, destinationUser)
                sockets[self.owner].send("Client %s is available for a chat session" % (destinationUser))

                while localstring[self.iterator] != "exit chat":                               #while the user doesn't end the chat...

                    localstring[self.iterator] = sockets[self.owner].recv(1024)                #receive line from client
                    sockets[destinationUser].send(localstring[self.iterator])

            else:
                sockets[self.owner].send("b not available")  # or else, print this and




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


BackgroundTask(count).start()
