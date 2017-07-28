from socket import *
from functions import *
import thread
import time
import threading


sessions = []                                               #array for each active chat
count = 0                                                   #counts how many threads/users have connected so far
serverPort = 12000
localstring = []                                            #array of string that is used by each thread
#creates hashmap of sockets
users = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
sockets = {}
for x in range (0, 9):
    sockets[users[x]] = socket(AF_INET, SOCK_STREAM)


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


                conn.send('CONNECTED')
                print 'User ' + newuser + " has connected to the server"



                print 'this is the ' + newuser
                go_online(newuser)
                print online

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
        #self.sock = sock
    def run(self):

        localstring.append('flks;ddksj')

        while 1:
            destinationUser = 'z'


            localstring[self.iterator] = sockets[self.owner].recv(1024)                        # receive line from client
            #G[0] = self.sock.recv(1024)
            print localstring[self.iterator]


            destinationUser = localstring[self.iterator]
            #if G[0] == 'CHAT':
            if destinationUser in online:
                print "entered chat"
                sockets[self.owner].send("Client %s is available for a chat session" % (destinationUser))


                while localstring[self.iterator] != "exit chat":                # while the user doesn't end the chat...

                    localstring[self.iterator] = sockets[self.owner].recv(1024)                # receive line from client
                    sockets[destinationUser].send(localstring[self.iterator])


                    #self.sock.send(fromClient)  # send line to other end
                    # write line to file
            else:
                sockets[self.owner].send("b not available")  # or else, print this and


BackgroundTask(count).start()
