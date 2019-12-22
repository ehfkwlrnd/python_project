from Crypto.Cipher import AES
import hashlib, time
import base64
from Crypto import Random

key = hashlib.sha256('0'.encode('utf-8')).digest()
bs = 16

def encrypt(origin):
    origin = origin.encode('utf-8')
    raw = origin + (bs - len(origin)%bs) * chr(bs-len(origin)%bs).encode('utf-8')

    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    enc = base64.b64encode(iv + cipher.encrypt(raw)).decode('utf-8')
    return enc

def decrypt(enc):
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    dec = cipher.decrypt(enc[AES.block_size:]).decode('utf-8')
    dec = dec[:-ord(dec[len(dec)-1:])]
    return dec

