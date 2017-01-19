from app import web, db
from datetime import datetime


class Story_Page_Content(db.Model):
    TYPE_AUTO = 'AUTO'
    TYPE_TEXT = 'TEXT'
    TYPE_IMAGE = 'IMAGE'
    TYPE_AUDIO = 'AUDIO'
    TYPE_VIDEO = 'VIDEO'
    TYPE_HTML = 'HTML'

    __tablename__ = 'story_page_content'

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    type = db.Column(db.String(128), nullable=False)
    body = db.Column(db.Text)
    additional_data = db.Column(db.Text)

    page = db.relationship('Story_Page', backref='content', uselist=False)
