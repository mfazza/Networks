#functions

userid = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]

def validate (x):
    "Checks to see if user has a valid id matching the ones on the list"
    isvalid = False
    for y in range (0, 9):
        if (x == userid[y]):
            isvalid = True
        else:
            continue
    return isvalid

