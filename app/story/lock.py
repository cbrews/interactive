from app import web, db
from datetime import datetime

class Story_Page_Lock(db.Model):
    TYPE_NONE = 'NONE'
    TYPE_PASSWORD = 'PASSWORD'
    TYPE_TIMESTAMP = 'TIMESTAMP'
    TYPE_GEOLOCATION = 'GEOLOCATION'
    TYPE_APPROVAL = 'APPROVAL'
    TYPE_UNIVERSAL = 'UNIVERSAL'

    __tablename__ = 'story_page_lock'

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    type = db.Column(db.String(128), nullable=False)
    key = db.Column(db.Text)
    additional_data = db.Column(db.Text)

    page = db.relationship('Story_Page', backref='lock', uselist=False)
