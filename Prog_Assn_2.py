import hmac 
from hashlib import md5 
from hashlib import sha1 
from hashlib import sha256
import hashlib

key = b'DECLARATION' 
h = hashlib.sha3_256()
h.update(b'A horse, a horse! My kingdom for a horse!')
h.digest()
print(h.hexdigest())
# content h.update(b'A horse, a horse! My kingdom for a horse!')
# print the Hash digest: MD5 print (h.hexdigest())