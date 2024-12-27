"""
SecureKey Vault - Utility Functions

Contains helper methods for encryption, decryption, and other library calls.
"""

def encrypt_secret(secret: str) -> str:
    """Fake encryption for demonstration."""
    return f"encrypted-{secret}"

def decrypt_secret(encrypted: str) -> str:
    """Fake decryption for demonstration."""
    if encrypted.startswith("encrypted-"):
        return encrypted.replace("encrypted-", "")
    return encrypted
