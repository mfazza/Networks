from socket import *

menu1 = 'sdkljfhds'                                     #variable for the first menu
user_Id = '1001'                                        #user id
HELLO = user_Id                                         #used this to make it more relatable to the project guideline
serverName = gethostname()                              #gets the name of the host (which is interface dependent)
serverPort = 12000                                      #100% arbitrary




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

if confirmation != "Connected": exit()


print "\nWelcome to Matt and Nick's Chat application.\nOnce you're connected to the server, these are some useful commands:\n"
print "1 - Chat Request: type 'HELLO' to request a chat with another user\n"
print "2 - History Request: request chat history between clients\n"
print "3 - End request: to end a request, type 'ENDREQ'.  *Works inside chat as well.\n\n"