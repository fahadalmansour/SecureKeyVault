import pytest
from src.utils import encrypt_secret, decrypt_secret

def test_encrypt_secret():
    result = encrypt_secret("test")
    assert result == "encrypted-test"

def test_decrypt_secret():
    result = decrypt_secret("encrypted-test")
    assert result == "test"
