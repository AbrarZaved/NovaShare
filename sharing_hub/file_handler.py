import os
from cryptography.fernet import Fernet
from django.conf import settings
import environ

env = environ.Env()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_file = os.path.join(BASE_DIR, ".env")
environ.Env.read_env(env_file)


ENCRYPTION_KEY = env("NOVASHARE_SECRET_KEY")
cipher = Fernet(ENCRYPTION_KEY)


def encrypt_file(file_content):
    return cipher.encrypt(file_content)


def decrypt_file(encrypted_content):
    return cipher.decrypt(encrypted_content)
