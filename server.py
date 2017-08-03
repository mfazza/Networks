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
        destinationUser = 'z'

        while 1:

            localstring[self.iterator] = sockets[self.owner].recv(1024)
            print localstring[self.iterator]

            if protocol[3] in localstring[self.iterator]:
                if localstring[self.iterator][13] != self.owner:
                    break

                destinationUser = localstring[self.iterator][15]
                print destinationUser
                if destinationUser not in online.keys():
                    sockets[self.iterator].send(protocol[5]) #unreachable
                    break
                elif online[self.owner] or online[destinationUser] != 0:
                    sockets[self.iterator].send(protocol[5])  # unreachable
                    break
                else:
                    create_chat(self.owner, destinationUser)
                    chatnumber = online[self.owner]
                    sockets[self.owner].send(protocol[4] + "(" + str(chatnumber) + "-" + self.owner + "-" + destinationUser + ")")
                    sockets[destinationUser].send(protocol[4] + "(" + str(chatnumber) + "-" + self.owner + "-" + destinationUser + ")")

            elif protocol[6] in localstring[self.iterator]:

                IDDD = int(str[12:16])
                for key in online.keys():
                    if online[key] == IDDD:
                        sockets[key].send(protocol[7] + IDDD)

                for key in online.keys():
                    if online[key] == IDDD:
                        online[key] = 0

            elif protocol[8] in localstring[self.iterator]:
                destuser = 'x'
                sessionid = int(localstring[self.iterator][5:9])
                print sessionid
                print online
                if sessionid in online.values():
                    for key in online.keys():
                        if online[key] == sessionid and key != self.owner:
                            print key
                            destuser = key

                            #writes string to file
                sockets[destuser].send(localstring[self.iterator][10:])

        #elif protocol[9] in localstring[self.iterator]:
            #gets sessionid from HIST_REQclient1client2




BackgroundTask(count).start()
