from functools import wraps
from flask import abort, request

class Auth:
    TOKEN_HEADER = 'x-auth'
    def validate(self, fn):

        @wraps(fn)
        def tokenVerification(*args, **kwargs):
            from user import User

            user = User.getTokenUser(self.getToken())

            if user is not None:
                return fn(*args, **kwargs)
            else:
                abort(401)

        return tokenVerification

    def getToken(self):
        if self.TOKEN_HEADER not in request.headers:
            return ""
        return request.headers[self.TOKEN_HEADER]
