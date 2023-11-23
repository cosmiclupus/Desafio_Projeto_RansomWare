import os
import pyaes

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as file:
        ciphertext = file.read()

    aes = pyaes.AESModeOfOperationCTR(key)
    plaintext = aes.decrypt(ciphertext)

    os.remove(file_name)

    new_file_name = file_name.replace(".ransomwaretroll", "_decrypted.txt")
    with open(new_file_name, 'wb') as new_file:
        new_file.write(plaintext)


key = b"testeransomwares" 
file_to_decrypt = "teste.txt.ransomwaretroll"


decrypt_file(file_to_decrypt, key)