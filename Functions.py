#functions
from socket import *


userid = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
sPorts = ['a', 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020]
serverName = gethostname()

def validate (x):
    "Checks to see if user has a valid id matching the ones on the list"
    isvalid = False
    for y in range (0, 9):
        if (x == userid[y]):
            isvalid = True
        else:
            continue
    return isvalid

def get_sport():
    if len(sPorts) == 0:
        return 'no port available'
    else:
        portNo = sPorts[0]
        del sPorts[0]
        return portNo


def serverThread(socket1, socket2):

    buffersize = 1024
    msg1 = ''
    msg2 = ''


    while 1:

        msg1 = socket1.recv(buffersize)
        msg2 = socket2.recv(buffersize)
        socket1.send(msg2)
        socket2.send(msg1)
