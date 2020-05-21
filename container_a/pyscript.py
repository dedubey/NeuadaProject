import base64
import time
from cryptography.fernet import Fernet
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import shutil 
import sys 
var1=sys.argv[1] 
from dicttoxml import dicttoxml 
import json
import pandas as pd 
from shutil import copyfile

    

data_df = pd.read_json('/work/source/{}'.format(var1), orient='records')
df = pd.DataFrame(data_df, columns=data_df.keys())


data_dict = df.to_dict(orient="records")
print("Converting to XML")
xml_data = dicttoxml(data_dict).decode()
with open("/work/source/{}.xml".format(var1), "w+") as f:
    f.write(xml_data)
print("XML file created")
time.sleep(3)
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

print(key)

input_file = '/work/source/{}.xml'.format(var1)
output_file = '/work/source/{}.enc'.format(var1)

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)



shutil.move('/work/source/{}.enc'.format(var1),'/work/shared/')
print("Encrupted File sent to shared folder")

#os.remove('./source/{}.xml'.format(var1))
