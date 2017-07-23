''''#server side
#the server verifies has an ID on the list of subscribers'''

from socket import *
from Functions import *
from thread import *
import time
import threading



count = 0                                                   #this is an iterator for the list of sockets
forwardPort = 0                                             #this is the port that will be used for the creation of new sockets once the user connects
individualSockets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]         #array of sockets (couldn't make it work without explicitly filling it up)
availableUsers = {}                                         #dictionary of users availble --- [user: port]  -- think of it like a hashmap
arrayT = []
arrayT2 = []


#function to go into thread
def __outer_thread__(pNumber, iteration):                   #the function takes a port number, and the index of the array of sockets
    print "outer thread working"

    individualSockets[iteration] = socket(AF_INET, SOCK_STREAM)
    individualSockets[iteration].bind(('', pNumber))
    individualSockets[iteration].listen(1)                  #socket creation, binding, and listening
    conn, addr = individualSockets[iteration].accept()      #this line took most of my day.  You have to make it explicit that the socket is ready to receive


    while 1:                                                #does this forever
        destinationUser = 'z'
        time.sleep(0.2)                                         #pretty mystic, but it only works if there's a slight delay between iterations
        fromClient = conn.recv(1024)                            #receive line from client

        if fromClient in availableUsers.keys():                 #I worked out a simple validation to make the sockets and the dictionary work
            destinationUser = fromClient
            if availableUsers.has_key(destinationUser):                         #if key 'b' is in availableusers... That is: if user b is available to chat

                conn.send("Client xxx is available for a chat session")
                #chatSession = getSession()                      #get chat session
                destinationNumber = availableUsers[destinationUser]

                while fromClient != "exit chat":                #while the user doesn't end the chat...
                    fromClient = conn.recv(1024)                #receive line from client
                    print fromClient
                    conn.sendto(fromClient,  (gethostname(), destinationNumber))    #send line to other end
                                                               #write line to file
            else:
                conn.send("b not available")                #or else, print this and

def __main__thread(count):

    while 1:
        connectionSocket,addr=serverSocket.accept()             #Will indefinitely accept data from clients
        user_Request = connectionSocket.recv(1024)              #receive (buffer size of 1024 bytes)
        validation = validate(user_Request)                     #the validation function is in the Functions.py file.  It checks the userID for validation


        #validation part
        if validation == True:                                  #if user connects successfully they receive a port number and new thread is created
            connectionSocket.send("Connected")
            print 'User ' + user_Request + " has connected to the server"

            forwardPort = get_sport()                           #call get_sport function to get a port from the available ones
            connectionSocket.send(str(forwardPort))             #send the port to the client so they know where to connect


            availableUsers.update({user_Request: forwardPort})  #updates the dictionary with [the authenticated user: their port number]
                                                                #then starts new thread that is going to run the __outer__thread__ function
            #thread.start_new_thread(__outer_thread__(forwardPort, count))
            #arrayT2 = threading.Thread(target = __outer_thread__(forwardPort, count))

            arrayT2[count] = threading.Thread(target=__outer_thread__(forwardPort, count))
            arrayT2[count].setDaemon(True)
            arrayT2[count].run()

            ###IT HALTS HERE
            print 'created outer thread'

            count += 1                                          #updates count
            arrayT[count] = threading.Thread(target=__main__thread(count))
            arrayT[count].setDaemon(True)
            arrayT[count].run()
            print 'created new main thread'
        else:
            connectionSocket.send("User id not valid\n")



serverPort = 12000                                          #The port used by the host to connect to the server
serverSocket = socket(AF_INET, SOCK_STREAM)                 #creates socket and on the next line, binds it to a port
serverSocket.bind(('', serverPort))                         #leaving the first member of the tuple as '' denotes the welcoming socket
serverSocket.listen(1)                                      #ready to receive data from client
print "The server is ready to receive"


arrayT[count] = threading.Thread(target = __main__thread(count))
arrayT[count].setDaemon(True)
arrayT[count].run()
#threading.Thread(target = __main__thread(count)).start()

#thread.start_new_thread(__main__thread(count))
