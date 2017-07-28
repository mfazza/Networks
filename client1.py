from socket import *
import time
import threading
import functions

menu1 = 'sdkljfhds'                                     #variable for the first menu
user_Id = 'a'                                           #user id
HELLO = user_Id                                         #used this to make it more relatable to the project guideline
#serverName = gethostname()                              #gets the name of the host (which is interface dependent)
serverName = gethostbyname("localhost")
serverPort = 12000                                      #100% arbitrary
receivedPort = 0

class receiving(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        while 1:
            output = clientSocket.recv(1024)
            print output + '\n'



class sending(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            togo = raw_input()
            #print togo
            clientSocket.send(togo)




'''First menu'''
while menu1 not in ['log on', 'disconnect']:
    menu1 = raw_input("Please enter 'log on' to connect to the server or 'disconnect' to leave.\n")

if menu1 == "disconnect":
    exit()

clientSocket = socket(AF_INET, SOCK_STREAM)             #creates socket
clientSocket.connect((serverName, serverPort))          #connects to server's socket
clientSocket.send(HELLO)                                #validates server
confirmation = clientSocket.recv(1024)                  #receives confirmation from server
print 'server: ' + confirmation                         #displays confirmation from server
if confirmation != "CONNECTED":
    clientSocket.close()
    exit()

#at this point the server will receive the port for the chatsocket

time.sleep(1)                                           #again, it only works after a slight delay

tosend = sending()
tosend.start()
toreceive = receiving()
toreceive.start()


#while 1:                                                #runs forever
#    clientSocket.send(raw_input())                     #gets input from keyboard
#    print 'server: ' + clientSocket.recv(1024)         #prints what the thread running "__outer__thread__ is sending



