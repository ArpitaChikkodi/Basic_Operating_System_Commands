""""
Author : Arpita Chikkodi
Date : August 2 2021
Description : This script is used to encrypt any password and store the key in a file, to decrypt both the encrypted message and key file are required
"""
from cryptography.fernet import Fernet
from getpass import getpass

def generate_key(filepath):
    """
    Generates a key and save it into a file
    Ex : filepath => "password_bang_site.key"
    """
    key = Fernet.generate_key()
    with open(filepath, "wb") as key_file:
        key_file.write(key)

def load_key(filepath):
    """
    Load the previously generated key into the file
    """
    return open(filepath, "rb").read()

def encrypt_message(message,filepath):
    """
    Encrypts a message
    """
    key = load_key(filepath)
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    print("\nThe encrypted message is printed below, please copy it!")
    print(encrypted_message)


def decrypt_message(encrypted_message,filepath):
    """
    Decrypts an encrypted message
    """
    key = load_key(filepath)
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    print(decrypted_message.decode())

if __name__ == "__main__":
    print("\nTo encrypt a unix password for updating LDAP, please follow the below steps : \n1.Give filepath path where the key file should be stored \n2.Enter the password to be encrypted \n3.Copy the encrypted message that is printed on the console when this script is executed \n4.Remember the file path where key is stored \n5.The filepath and encrypted message should be updated in config.py file")
    filepath = input("\nEnter filepath where key should be stored(give absolutepath if not in same directory) Ex: '/u1/apps/vmbuild/app/abc.key') : ")
    password = getpass("Enter password to be encrypted : ")
    generate_key(filepath)
    message = encrypt_message(password,filepath)



""" To encrypt"""
# if __name__ == "__main__":
#     #generate_key()
#     #message = encrypt_message("")


"""To decrypt"""
# if __name__ == "__main__":
#     decrypt_message(b'gAAAAABesCUIAcM8M-_Ik_-I1-JD0AzLZU8A8-AJITYCp9Mc33JaHMnYmRedtwC8LLcYk9zpTqYSaDaqFUgfz-tcHZ2TQjAgKKnIWJ2ae9GDoea6tw8XeJ4=',filepath)



##############################################Decrypting######################################


def load_key(path):
    """
    Load the previously generated key
    """
    return open(path, "rb").read()

def decrypt_message(encrypted_message,secretkeypath):
    """
    Decrypts an encrypted message
    """
    key = load_key(secretkeypath)
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()
    

#call
credential = decrypt_message(config.password_encrypted,config.password_secretkey_path)
