from app import web, db
from app.core.model import Core

class Story_Page_Lock(Core):
    TYPE_NONE = 'NONE'
    TYPE_PASSWORD = 'PASSWORD'
    TYPE_TIMESTAMP = 'TIMESTAMP'
    TYPE_GEOLOCATION = 'GEOLOCATION'
    TYPE_APPROVAL = 'APPROVAL'
    TYPE_UNIVERSAL = 'UNIVERSAL'

    __tablename__ = 'story_page_lock'

    type = db.Column(db.String(128), nullable=False)
    key = db.Column(db.Text)
    additional_data = db.Column(db.Text)

    page = db.relationship('Story_Page', backref='lock', uselist=False)
