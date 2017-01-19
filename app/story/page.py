from app import web, db
from datetime import datetime
from app.cryptography import Serializer, random_string

class Story_Page(db.Model):
    __tablename__ = 'story_page'

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    next_id = db.Column(db.Integer, db.ForeignKey('story_page.id'))
    hash = db.Column(db.String(256), nullable=False, unique=True)
    secret_key = db.Column(db.String(4096), nullable=False)
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'), nullable=False)
    content_id = db.Column(db.Integer, db.ForeignKey('story_page_content.id'))
    lock_id = db.Column(db.Integer, db.ForeignKey('story_page_lock.id'))

    def __init__(self, **kwargs):
        self.hash = random_string(64) # Not sure if this is necessarily unique enough, TBD
        print len(self.hash)
        self.secret_key = random_string(2048)
        print len(self.secret_key)

        super(Story_Page, self).__init__(**kwargs)

    def getSignedToken(self, uuid):
        return Serializer(self.secret_key).create_token(uuid)

    def authenticateHash(self, token):
        return Serializer(self.secret_key).validate_token(token)
