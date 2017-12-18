#Feistel.py created by Mathews Fazza
#This file provides the functions that are used by Client.py


import time
from hashlib import sha512
import base64

subkeys = []                                            #array of subkeys derived from the real key
rounds = 2                                              #number of times plaintext goes through the Feistel cipher


def generateSubkeys(key, rounds):
    for x in range(rounds):                             #every round in the Feistel cipher requires a subkey.
                                                        #This generates those subkeys.
        subHash = sha512(key + str(x)).hexdigest()      #to create a subkey, append a new int to it and hash it
        subkeys.append(oct(int(subHash, 16))[2:])       #adds element in list of subkeys in octal format
    #print "subkeys: " + str(subkeys)


def padBinary(binary, paddingLen):                      #we need to make sure the binary strings only have 8 bits.
    padding = ""                                        #so we pad the strings that don't.
    for a in range(paddingLen - len(binary)):           #repeat for the difference between 8 and the current length
        padding += "0"
    return padding + binary


def rotateByte(rotatingNumber, rotationNumber):         #byte rotation for a single byte
    rotatedNumber = getBinary(rotatingNumber, 8)[int(rotationNumber) % 8:] + getBinary(rotatingNumber, 8)[
                                                                             :int(rotationNumber) % 8]
    return int(rotatedNumber, 2)


def rotateBits(plainText, subkey):                      #general byte rotation and 0 stripping
    octPlainText = []
    for a in plainText:
        octPlainText.append([])
    for characterIndex in range(len(plainText)):
        octCharacter = oct(plainText[characterIndex])
        for digit in octCharacter[1:]:
            octPlainText[characterIndex].append(digit)

    xoredPlainText = []
    keyIndex = 0
    for character in octPlainText:

        octCharacter = ""
        for digit in character:
            octCharacter += oct(int(digit) ^ int(subkey[keyIndex % len(subkey)]))[1:]
            keyIndex += 1

        try:
            xoredPlainText.append(int(octCharacter, 8))
        except ValueError:
            octCharacter = oct(0)
            xoredPlainText.append(int(octCharacter, 8))

    return xoredPlainText


def shuffleBlock(block, subkey):                        #uses subkey of the round to shuffle plaintext
    shuffledBinaryBlock = [[], [], [], [], [], [], [], []]
                                                        #Since subkeys are in octal, this is a list of 8 lists.
                                                        #the corresponding byte in the subkey determines where the
                                                        #bit will be placed within the lists
    binaryBlock = ""
    for a in block:                                     #loop for binary conversion
        binaryBlock += getBinary(a, 8)
    for a in range(len(binaryBlock)):                   #loop for shufflingshuffling
        shuffledBinaryBlock[int(subkey[a % len(subkey)])].append(binaryBlock[a])
    shuffledBlock = ""
    for a in shuffledBinaryBlock:                       #loop to conver shuffledBinaryBlock into a string
        for b in a:
            shuffledBlock += b
    shuffledBlockList = []
    for a in range(len(block)):  # /len(block)):
        shuffledBlockList.append(
            int(shuffledBlock[a * 8:(a + 1) * 8], 2))   #makes shuffledBlock into a list of integers
    return shuffledBlockList                            #returns the list of integers


def round(subkey, right):                               #function to shuffle and rotate the right side before Xoring
                                                        #with the left
    rightA = rotateBits(right, subkey)
    rightB = shuffleBlock(rightA, subkey)
    return rightB                                       #return final obfuscation


def split(plainText):                                   #splits the plaintext into two parts and pads with a nullbyte
                                                        # if plaintext is odd
    if len(plainText) % 2 == 0:                         #if plaintext is even
        left = plainText[:len(plainText) / 2]
        right = plainText[len(plainText) / 2:]
    else:                                               #if plaintext is odd
        plainText.append(0)
        left = plainText[:len(plainText) / 2]
        right = plainText[len(plainText) / 2:]
    return left, right                                  #return both halves


def exclusiveOr(left, newRight):                        #makes left an XOR of right that has gone through round function
    newLeft = []
    for a in range(len(left)):                          #iterates one by one
        newLeft.append(newRight[a] ^ left[a])
    return newLeft                                      #returns left(now an XOR of right that has been through "round")


def encrypt(plainText, subkeys):                        #function that puts everything together
    left, right = split(plainText)                      #plaintext split
    #print("left: " + str(left) + " right: " + str(right))
    for x in range(rounds - 1):                         #iterates (number of rounds - 1) times
        newRight = round(subkeys[x][:-1], right)        #run the round function
        left = exclusiveOr(left, newRight)              #make left the XOR of newRight
        left, right = right, left                       #swap left and right
        #print("left: " + str(left) + " right: " + str(right))
    newRight = round(subkeys[rounds - 1][:-1], right)   #a final round (without the swap at the end)
    left = exclusiveOr(left, newRight)
    #print("left: " + str(left) + " right: " + str(right))
    cipherText = left + right
    #print "cipher text "
    #print cipherText
    return cipherText                                   #return ciphertext as a list of int


def getAscii(plainText):                                #conversion of plainText into ascii integers
    asciiText = [ord(c) for c in plainText]
    return asciiText


def getBinary(decimal, padding):                        #binary conversion
    decimal = int(decimal)
    binary = ''
    if decimal == 0: decimal = 0
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal >> 1
    binary = padBinary(binary, padding)                 #binary might need to padded to have length of 8
    return binary




def outputCipherText(cipherText, direction):            #function to build output

    if direction == "e":                                #if we are encrypting
        asciiCipherText = ""
        for a in cipherText:                            #converts the list of integers that is cipherText to ascii str
            asciiCipherText += chr(a)
        base64CipherText = base64.b64encode(asciiCipherText)
                                                        #converts ascii string into base 64
        return base64CipherText                         #returns base 64 cipher text

    else:                                               #if decrypting
        asciiPlainText = ""
        for a in cipherText:                            #converts cipherText to an ascii string
            if not chr(a) == chr(0):                    #provided it's not a nullbyte which we used to pad
                asciiPlainText += chr(a)
        return asciiPlainText                           #returns plaintext



def feistelAtWork(plainText, key, direction):           #function the clients call when using the Feistel cipher

    #here we could add something to pad the string to have a length multiple of 8


    if(len(plainText)%8 != 0):
        for x in range(8 - (len(plainText)%8)):
            plainText += " "

    asciiPlainText = getAscii(plainText)                #get list of the characters in ascii decimals


    generateSubkeys(key, rounds)                        #generate subkeys based on key

    if direction == "e":                                #if encrypting
        cipherText = encrypt(asciiPlainText, subkeys)   #plaintext encryption

    else:                                               #if decrypting
        asciiPlainText = getAscii(base64.b64decode(plainText))
                                                        #decode from the base 64 format
        cipherText = encrypt(asciiPlainText, list(reversed(subkeys)))
                                                        #encrypt with the reversed subkeys (which means decrypting)

    return outputCipherText(cipherText, direction)      #returns string of
