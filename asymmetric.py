from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os

# Generate and save a private/public key pair
def generate_keys(private_key_file='private_key.pem', public_key_file='public_key.pem'):
    # Generate a private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Generate the corresponding public key
    public_key = private_key.public_key()

    # Serialize and save the private key
    with open(private_key_file, 'wb') as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Serialize and save the public key
    with open(public_key_file, 'wb') as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    print(f"Keys generated and saved to {private_key_file} and {public_key_file}")

# Load the private key
def load_private_key(private_key_file='private_key.pem'):
    with open(private_key_file, 'rb') as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None,
        )
    return private_key

# Load the public key
def load_public_key(public_key_file='public_key.pem'):
    with open(public_key_file, 'rb') as f:
        public_key = serialization.load_pem_public_key(
            f.read(),
        )
    return public_key

# Encrypt a file using the public key
def encrypt_file(file_path, public_key):
    with open(file_path, 'rb') as file:
        original_data = file.read()

    # Encrypt the data using the public key
    encrypted_data = public_key.encrypt(
        original_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save the encrypted data to a new file
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"File encrypted and saved as {encrypted_file_path}")

# Decrypt a file using the private key
def decrypt_file(encrypted_file_path, private_key):
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the data using the private key
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save the decrypted data to a new file
    decrypted_file_path = encrypted_file_path[:-4]  # Remove '.enc' from the filename
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"File decrypted and saved as {decrypted_file_path}")

# Main function
def main():
    private_key_file = 'private_key.pem'
    public_key_file = 'public_key.pem'

    # Generate keys if they don't exist
    if not os.path.exists(private_key_file) or not os.path.exists(public_key_file):
        generate_keys(private_key_file, public_key_file)

    # Load keys
    private_key = load_private_key(private_key_file)
    public_key = load_public_key(public_key_file)

    while True:
        print("\nFile Encryption/Decryption Tool (Asymmetric)")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            file_path = input("Enter the path of the file to encrypt: ")
            if os.path.exists(file_path):
                encrypt_file(file_path, public_key)
            else:
                print("File not found!")
        elif choice == '2':
            file_path = input("Enter the path of the encrypted file to decrypt: ")
            if os.path.exists(file_path):
                decrypt_file(file_path, private_key)
            else:
                print("File not found!")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
