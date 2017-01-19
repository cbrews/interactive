from app import web, db
from werkzeug.security import generate_password_hash, check_password_hash
from app.cryptography import Serializer

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(256))

    def __init__(self, username, password):
        self.username = username
        self.password = self.hashword(password)

    def hashword(self, password):
        return generate_password_hash(password, salt_length=32)

    def verifyHashword(self, password):
        return check_password_hash(self.password, password)

    def generateToken(self):
        return Serializer(web.config["SECRET_KEY"]).create_token({"username": self.username})

    @classmethod
    def getByUsername(this, username):
        return this.query.filter_by(username=username).first()

    @classmethod
    def getAuthUser(this, username, password):
        user = this.getByUsername(username)
        if user and user.verifyHashword(password):
            return user
        else:
            return None

    @classmethod
    def getTokenUser(this, token):
        data = Serializer(web.config["SECRET_KEY"]).validate_token(token)

        if data:
            return this.getByUsername(data['username'])
        return None
