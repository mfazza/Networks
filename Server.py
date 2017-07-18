''''#server side

#the server verifies has an ID on the list of subscribers'''

from socket import *
from Functions import *



serverPort = 12000                                          #The port used by the host to connect to the server
serverSocket = socket(AF_INET,SOCK_STREAM)                  #creates socket and on the next line, binds it to a port
serverSocket.bind(('', serverPort))                         #leaving the first member of the tuple as '' denotes the welcoming socket
serverSocket.listen(1)                                      #ready to receive data from client
print "The server is ready to receive"
while 1:
    connectionSocket,addr=serverSocket.accept()             #Will indefinitely accept data from clients
    user_Request = connectionSocket.recv(1024)              #receive (buffer size of 1024 bytes)
    validation = validate(int(user_Request))                #the validation function is in the Functions.py file.  It checks the userID for validation
    if validation == True:
        connectionSocket.send("Connected")
        print user_Request + " connected to the server"
    else:
        connectionSocket.send("User id not valid\n")
        #needs to deny connection to client

        #we also need to define what else the server does once someone connects (such as add their user id to a list, check available history, etc.)




