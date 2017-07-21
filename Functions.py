#functions
from socket import *

it = 0
userid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
sPorts = [12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020]
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

# for it in range (12010, 12022):
#     try:
#         print sPorts.index(it)
#     except ValueError:
#         print "not found"
