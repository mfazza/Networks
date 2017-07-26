from socket import *
from functions import *
import thread
import time
import threading

global G
G = ['', '', '', '', '']                                    #my idea was for every chat to use a global string that can be changed by both end points
sessions = []
count = 0
serverPort = 12000
localstring = []
lock1 = threading.Lock()



serverSocket = socket(AF_INET, SOCK_STREAM)                 #creates socket and on the next line, binds it to a port
serverSocket.bind(('', serverPort))                         #leaving the first member of the tuple as '' denotes the welcoming socket
serverSocket.listen(1)                                      #ready to receive data from client
print "The server is ready to receive"


class BackgroundTask(threading.Thread):

    def __init__(self, iterator):
        threading.Thread.__init__(self)
        self.iterator = iterator


    def run(self):
        while 1:
            conn, addr = serverSocket.accept()  # Will indefinitely accept data from clients
            newuser = conn.recv(1024)  # receive (buffer size of 1024 bytes)
            validation = validate(newuser)  # It checks the userID for validation

            # validation part
            if validation == True:  #if user connects successfully they receive a port number and new thread is created
                conn.send('CONNECTED')
                print 'User ' + newuser + " has connected to the server"

                print 'this is the ' + newuser
                go_online(newuser)
                print online

                sessions.append(IndividualTask(self.iterator, conn))
                sessions[self.iterator].start()

                print threading.enumerate()

                self.iterator += 1  # updates count

            else:
                conn.send("DECLINED\n")

class IndividualTask(threading.Thread):
    def __init__(self, iterator, sock):
        threading.Thread.__init__(self)
        self.iterator = iterator
        self.sock = sock
    def run(self):

        localstring.append(G[0])

        while 1:
            destinationUser = 'z'


            # localstring[self.iterator] = self.sock.recv(1024)                        # receive line from client
            G[0] = self.sock.recv(1024)
            #print localstring[self.iterator]


            destinationUser = localstring[self.iterator]
            if G[0] == 'CHAT':
            #if destinationUser in online:
                print "entered chat"
                self.sock.send("Client %s is available for a chat session" % (destinationUser))


                while localstring[self.iterator] != "exit chat":                # while the user doesn't end the chat...
                    if localstring[self.iterator] != G[0]: self.sock.send(G[0])

                    localstring[self.iterator] = self.sock.recv(1024)                # receive line from client
                    lock1.acquire()
                    G[0] = localstring[self.iterator]
                    lock1.release()


                    #self.sock.send(fromClient)  # send line to other end
                    # write line to file
            else:
                self.sock.send("b not available")  # or else, print this and


BackgroundTask(count).start()