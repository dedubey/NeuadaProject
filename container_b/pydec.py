import base64
import shutil
import time
from cryptography.fernet import Fernet
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import sys
var1=sys.argv[1]
password_provided = "1234" 
password = password_provided.encode() 
salt = b'salt_' 
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password)) 

time.sleep(3)
print("Decrypting the file ")
time.sleep(2)
input_file = '/work/shared/{}'.format(var1)
output_file = '/work/shared/{}.xml'.format(var1)
#input_file = './shared/ex7.json.enc'                                                                                                                                                          input_file = 'ex9.json.xml.enc'
#output_file = './shared/{}.xml'.format(var1)

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)

print("Sending Decrypted File ")
shutil.move('/work/shared/{}.xml'.format(var1),'/work/destination/')
print("Encrupted File sent to shared folder")


