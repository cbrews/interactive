import os
import string

valid_chars = string.ascii_letters + string.digits

def random_string(length):
    return "".join(
        map(
            (lambda i: valid_chars[i % len(valid_chars)]),
            bytearray(os.urandom(length))
        )
    )
