from Feistel import *

print oct(23 + (7^5))

print "Pay attention, Nick.  This is how to use the function"
plain = "it can be literally anything"
key = "z"
direction = "e" #e for encrypt

#when encrypting
cipher = feistelAtWork(plain, key, direction)
print "encrypting '(The length of this string) mod 8 = 0   ': " + cipher

#when decrypting
backToPlain = feistelAtWork(cipher, key, "d")  #d for decrypt
print "decrypting " + cipher + ": " + backToPlain