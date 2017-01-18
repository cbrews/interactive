from app import web, db
from app.core.model import Core
from app.core.cryptography import random_string

class Story_Page(Core):
    __tablename__ = 'story_page'

    next_id = db.Column(db.Integer, db.ForeignKey('story_page.id'))
    hash = db.Column(db.String(256), nullable=False)
    secret_key = db.Column(db.String(2048), nullable=False)
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'), nullable=False)
    content_id = db.Column(db.Integer, db.ForeignKey('story_page_content.id'))
    lock_id = db.Column(db.Integer, db.ForeignKey('story_page_lock.id'))

    def __init__(self, **kwargs):
        self.hash = random_string(64)
        self.secret_key = random_string(2048)
        super(Story_Page, self).__init__(**kwargs)
