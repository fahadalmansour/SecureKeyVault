import pytest
from src.main import store_secret, retrieve_secret

def test_store_secret(capfd):
    store_secret("TEST", "value")
    out, _ = capfd.readouterr()
    assert "Stored secret 'TEST' with encrypted value: encrypted-value" in out

def test_retrieve_secret(capfd):
    retrieve_secret("TEST", "encrypted-value")
    out, _ = capfd.readouterr()
    assert "Retrieved secret 'TEST': value" in out
