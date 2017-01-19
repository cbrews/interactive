from itsdangerous import JSONWebSignatureSerializer, BadSignature, SignatureExpired

class Serializer:
    def __init__(self, secret_key):
        self._serializer = JSONWebSignatureSerializer(secret_key)

    def create_token(self, data):
        return self._serializer.dumps(data)

    def validate_token(self, token):
        try:
            return self._serializer.loads(token)
        except SignatureExpired:
            # Valid token but signature expired
            return None
        except BadSignature:
            # Invalid token
            return None
