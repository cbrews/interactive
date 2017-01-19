from app import web, db
from app.story import Story_Page
from datetime import datetime

class Story(db.Model):
    __tablename__ = 'story'

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    active = db.Column(db.SmallInteger)
    startdate = db.Column(db.DateTime)
    enddate = db.Column(db.DateTime)
    name = db.Column(db.String(128), nullable=False)
    first_page_id = db.Column(db.Integer, db.ForeignKey('story_page.id'))

    first_page = db.relationship("Story_Page", foreign_keys=[first_page_id])

    pages = db.relationship("Story_Page", backref="story", lazy="dynamic", foreign_keys=[Story_Page.story_id])

    def is_active(self):
        return self.active and (self.startdate is None or self.startdate <= datetime.now()) and (self.enddate is None or datetime.now() <= self.enddate)
