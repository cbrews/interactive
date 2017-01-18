from app import web, db
from app.core.model import Core

class Story_Page_Content(Core):
    TYPE_AUTO = 'AUTO'
    TYPE_TEXT = 'TEXT'
    TYPE_IMAGE = 'IMAGE'
    TYPE_AUDIO = 'AUDIO'
    TYPE_VIDEO = 'VIDEO'
    TYPE_HTML = 'HTML'

    __tablename__ = 'story_page_content'

    type = db.Column(db.String(128), nullable=False)
    body = db.Column(db.Text)
    additional_data = db.Column(db.Text)

    page = db.relationship('Story_Page', backref='content', uselist=False)
