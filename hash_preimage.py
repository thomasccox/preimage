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

    byte_sized = ceil(len(target_string)/8)
    remain = 7 - len(target_string)%8
    finalBits = ""

    while finalBits != target_string:
        bits = ""
        finalBits = ""
        a = os.urandom(64)
        hash_a = hashlib.sha256(a).digest()

        for i in range(len(hash_a)):
            str = bin(hash_a[i])
            '''
            if i == 32 - byte_sized:
                dif = 8 - len(str)
                start = remain - dif
                if start > 0:
                    for j in range(2+start, len(str)):
                        byte += str[j]
            #print(check)
            '''
            if len(str) < 10:
                #print(str)
                for j in range (10-len(str)):
                    bits+='0'
                    #print(bits)
            for k in range(2,len(str)):
                bits += str[k]
        for i in range(len(bits)-len(target_string), len(bits)):
            finalBits += bits[i];
            #print(bits)
        #print(target_string)
        #print(finalBits)


    return( a )