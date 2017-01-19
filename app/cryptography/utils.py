import secrets

def random_string(length):
    return secrets.token_urlsafe(length)
