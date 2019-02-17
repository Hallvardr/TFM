#!/usr/bin/env python2

import sys
import os.path
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import binascii

def print_help():
    print("Usage: python encrypt_decrypt_AES.py file_in [file_out]")
    print("  file_in: A path to the input file")
    print("  file_out (Optional): A path to a file to write the output")
    sys.exit(0)

# Check for the input file path
if len(sys.argv) == 1:
    # sys.argv always has the script path as the first index
    print_help()
else:
    if sys.argv[1] == '-v':
        print_help()
    else:
        in_path = sys.argv[1]
        if not os.path.isfile(in_path):
            print("Seems like the input path does not resolve to a file :(")
            sys.exit(2)

        if len(sys.argv) > 2:
            out_path = sys.argv[2]
            if not os.path.isfile(out_path):
                print("Given output path does not resolve to a file :('")
                print("Using defaults (" + in_path + ".out)")
                out_path = in_path + ".out"
        else:
            out_path = in_path + ".out"

# Preparing the input file
try:
    in_file = open(in_path, "r")
except IOError:
    print("Can't read the input file. You sure you have the right permissions to do it? :)")
    sys.exit(3)

# Preparing the output file
try:
    out_file = open(out_path, "w")
except IOError:
    print("Can't create the output file (" + out_path + "). You sure you have the right permissions to do it? :)")
    sys.exit(3)

enc_key = get_random_bytes(16)
cipher = AES.new(enc_key, AES.MODE_CBC)

print("================================================================")
print("!!! IMPORTANT !!!")
print("Key used to encrypt: " + binascii.hexlify(enc_key).upper())
print("If you loose the key you won't be able to decrypt the data back!")
print("================================================================")

# Get the list of words in the file
words = [word for line in in_file for word in line.split()]
for word in words:
    # Esta parte de aqui es la que encripta palabra por palabra y genera el resultado encriptado con la clave
    # random generada arriba en enc_key
    ct_bytes = cipher.encrypt(pad(word, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')

    # A ti lo unico que te interesará será la variable ct, creo
    result = json.dumps({'iv': iv, 'ciphertext': ct})
    out_file.write(result)

# Closing the files
in_file.close()
out_file.close()