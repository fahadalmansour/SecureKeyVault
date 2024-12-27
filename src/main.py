---

### 2.9 **src/main.py**

```python
"""
SecureKey Vault - Main Script

This script runs the core logic of the SecureKey Vault application.
It handles storing, retrieving, and encrypting secrets.
"""

from utils import encrypt_secret, decrypt_secret

def store_secret(secret_name: str, secret_value: str):
    """Store an encrypted secret in the system."""
    encrypted = encrypt_secret(secret_value)
    # Placeholder for storing in a database or file
    print(f"[INFO] Stored secret '{secret_name}' with encrypted value: {encrypted}")

def retrieve_secret(secret_name: str, encrypted_value: str):
    """Retrieve and decrypt a secret from the system."""
    decrypted = decrypt_secret(encrypted_value)
    print(f"[INFO] Retrieved secret '{secret_name}': {decrypted}")

if __name__ == "__main__":
    # Example usage
    secret_name = "API_TOKEN"
    secret_value = "super-secret-token-123"

    print("[INFO] Starting SecureKey Vault...")

    store_secret(secret_name, secret_value)
    # In a real scenario, you'd fetch the encrypted_value from a database
    example_encrypted_value = "encrypted-super-secret-token-123"
    retrieve_secret(secret_name, example_encrypted_value)
