import hashlib
import os
from math import ceil


def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    #nonce = b'\x00'

    trim = ""

    index = target_string.find('1')
    if index == -1:
        trim = "0"
    else:
        for i in range(index, len(target_string)):
            trim += target_string[i]

    byte_sized = ceil(len(target_string)/4)
    #print(byte_sized)
    byte = ""


    while byte != trim:
        a = os.urandom(64)
        hash_a = hashlib.sha256(a).digest()
        byte = ""
        for i in range(32-byte_sized, 32):
            str = bin(hash_a[i])
            #print(check)
            for j in range(2,len(str)):
                byte += str[j]
        print(byte)
        print(target_string)
    '''
    if len(byte) < len(target_string):
        lead = ""
        for j in range(len(target_string) - len(byte)):
            lead += '0'
        byte = lead + byte
    #print(byte)
    '''
    return( a )
