def encrypt(value, key):
    trans = ''
    i = 0
    j = 1
    for e in value:
        trans += chr(((ord(e) + (key + i)*j)-32)%96+32)
        i += 1
        j *= -1
    return trans

def decrypt(value, key):
    origin = ''
    i = 0
    j = -1
    for e in value:
        origin += chr(((ord(e) + (key + i)*j)-32)%96+32)
        i += 1
        j *= -1
    return origin
