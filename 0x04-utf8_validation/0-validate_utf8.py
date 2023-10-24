#!/usr/bin/python3
'''
UTF-8 Validation
'''


def validUTF8(data):
    ''' Returns True if data is a valid UTF-8 encoding, otherwise False '''
    num = 0
    for x in data:
        if num == 0:
            if x & 128 == 0:
                num = 0
            elif x & 224 == 192:
                num = 1
            elif x & 240 == 224:
                num = 2
            elif x & 248 == 240:
                num = 3
            else:
                return False
        else:
            if x & 192 != 128:
                return False
            num -= 1
    if num == 0:
        return True
    return False
