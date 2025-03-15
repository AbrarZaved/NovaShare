from cryptography.fernet import Fernet

# Generate a new encryption key (Run once and store securely)
key = Fernet.generate_key()
print("Encryption Key:", key.decode())  # Save this key securely
