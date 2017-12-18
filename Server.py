#server.py
#Created by Mathews Fazza and Nickolas Ramos
#
#This is the message relaying server that works in conjunction with client.py.  As users connect to the listening socket
#this server creates new sockets to receive their messages.  Those sockets exist in the 'sockets' array.
#Upon connecting, every user gets assigned their own thread that relays the messages using protocol messages
#
#Ctrl + Z will terminate this program on any machine (Windows, Linux, MAC OS)


from socket import *
from Functions import *
import thread
import time
import threading
import os

localstring = []                                            #array of string that is used by each thread
sessions = []                                               #array of individual threads (one per client)
count = 0                                                   #simple iterator to be used by all threads


users = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']  #creates dictionary of sockets objects
sockets = {}
for x in range (0, 9):
    sockets[users[x]] = socket(AF_INET, SOCK_STREAM)        #sockets will be created by the listening socket later


serverPort = 12000                                          #chosen port
serverSocket = socket(AF_INET, SOCK_STREAM)                 #creates socket and on the next line, binds it to a port
serverSocket.bind(('', serverPort))                         #This is the listening socket
serverSocket.listen(1)                                      #ready to receive data from client

class BackgroundTask(threading.Thread):                     #This class overrides the __init__  and the run methods
                                                            #of the threading class
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.i = i


    def run(self):
        while 1:
            conn, addr = serverSocket.accept()              #Will indefinitely accept data from clients
            newuser = conn.recv(1024)                       #receive (buffer size of 1024 bytes)
            validation = validate(newuser)                  #It checks the userID for validation
            sockets[newuser] = conn                         #passes object to dictionary 'a': socket

            # validation part
            if validation == True:                          #if user connects successfully they receive a port number
                                                            #and new thread is created

                conn.send(protocol[2])                      #sends "CONNECTED" to the user

                go_online(newuser)                          #function that logs users into the server

                sessions.append(IndividualTask(newuser, self.i))
                sessions[self.i].start()                    #once the new user connects, it gets its own thread


                self.i += 1                                 #updates count

            else:
                conn.send("DECLINED\n")

class IndividualTask(threading.Thread):                     #overrides __init__ and run from threading
    def __init__(self, owner, iterator):
        threading.Thread.__init__(self)
        self.iterator = iterator
        self.owner = owner

    def run(self):

        localstring.append('flks;ddksj')                    #each thread created has one string used for all operations
        destinationUser = 'z'                               #destination user is used to

        while 1:                                            #Thread will run until the user send a "log out" message

            localstring[self.iterator] = sockets[self.owner].recv(1024) #receives string from user and decides what
                                                                        #to do based on the protocol


            # if protocol == "CHAT_REQUEST"
            if protocol[3] in localstring[self.iterator]:
                if localstring[self.iterator][13] != self.owner:        #checks if request being made matches user
                    sockets[self.owner].send(protocol[5])               #making request.  Sends "UNREACHABLE" if not

                destinationUser = localstring[self.iterator][15]        #receives destination user from protocol

                if destinationUser not in online.keys():                #if destination user not online
                    sockets[self.owner].send(protocol[5])               #sends "UNREACHABLE" to requesting user

                elif online[self.owner] or online[destinationUser] != 0:    #if users are already engaged in another
                    sockets[self.owner].send(protocol[5])                   #chat, sends "UNREACHABLE" to them
                else:
                    create_chat(self.owner, destinationUser)            #creates chat
                    chatnumber = online[self.owner]                     #retrives chat number from online dictionary
                                                                        #then sends CHAT_STARTED to both users
                    sockets[self.owner].send(protocol[4] + "(" + str(chatnumber) + "-" + self.owner + "-" + destinationUser + ")")
                    sockets[destinationUser].send(protocol[4] + "(" + str(chatnumber) + "-" + self.owner + "-" + destinationUser + ")")


            #if protocol == END_REQUEST
            elif protocol[6] in localstring[self.iterator]:

                IDDD = int(localstring[self.iterator][12:16])           #gets session number from protocol
                for key in online.keys():                               #if session number is in online.values()
                    if online[key] == IDDD:
                        sockets[key].send(protocol[7] + "(" + str(IDDD) + ")")  #sends notification to users

                for key in online.keys():                               #this loop will reset the values of
                    if online[key] == IDDD:                             #online[user in chat] to 0, indicating they are
                        online[key] = 0                                 #online and available


            #if protocol == TALK
            elif protocol[8] in localstring[self.iterator]:
                destuser = 'x'                                          #initializes destuser
                sessionid = int(localstring[self.iterator][5:9])        #retrives chat session number from protocol

                if sessionid in online.values():                        #if session id that came in the protocol exists
                    for key in online.keys():                           #find the users associated with that session id
                        if online[key] == sessionid and key != self.owner:

                            destuser = key                              #finds the actual destination user
                            #writes string to file
                sockets[destuser].send(localstring[self.iterator][10:]) #sends string to the right user

                print "from " + self.owner + ": " + localstring[self.iterator][10:]

                                                                        #then writes to each user's file
                createChatHistory(self.owner, destuser, sessionid, self.owner, localstring[self.iterator][10:])
                createChatHistory(destuser, self.owner, sessionid, self.owner, localstring[self.iterator][10:])

            #if protocol == HISTORY_REQ
            elif protocol[9] in localstring[self.iterator]:

                f = open("logs/" + str(self.owner) + "-" + localstring[self.iterator][14])  #opens file if it exists
                for line in f:
                    sockets[self.owner].send(line)                                          #sends each line to client
                f.close()                                                                   #closes file

            #if protocol = 'log out'
            elif protocol[11] in localstring[self.iterator]:
                sockets[self.owner].send(protocol[11])
                sockets[self.owner].close()                             #closes socket
                del online[self.owner]                                  #Makes the user offline
                break                                                   #breaks from "while 1:" so thread can end
                #then break

BackgroundTask(count).start()                                           #starts background task.
