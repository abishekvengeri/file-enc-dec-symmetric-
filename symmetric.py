from cryptography.fernet import Fernet
import os

# Function to generate and save a key
def generate_key(key_file='secret.key'):
    key = Fernet.generate_key()
    with open(key_file, 'wb') as key_file:
        key_file.write(key)

# Function to load the key
def load_key(key_file='secret.key'):
    return open(key_file, 'rb').read()

# Function to encrypt a file
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original_data = file.read()
    encrypted_data = fernet.encrypt(original_data)
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"File encrypted and saved as {file_path}.enc")

# Function to decrypt a file
def decrypt_file(encrypted_file_path, key):
    fernet = Fernet(key)
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(encrypted_file_path[:-4], 'wb') as decrypted_file:  # Remove '.enc' from the filename
        decrypted_file.write(decrypted_data)
    print(f"File decrypted and saved as {encrypted_file_path[:-4]}")

# Main function
def main():
    key_file = 'secret.key'
    if not os.path.exists(key_file):
        generate_key(key_file)
    key = load_key(key_file)

    while True:
        print("\nFile Encryption/Decryption Tool")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            file_path = input("Enter the path of the file to encrypt: ")
            if os.path.exists(file_path):
                encrypt_file(file_path, key)
            else:
                print("File not found!")
        elif choice == '2':
            file_path = input("Enter the path of the encrypted file to decrypt: ")
            if os.path.exists(file_path):
                decrypt_file(file_path, key)
            else:
                print("File not found!")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
