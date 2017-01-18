from app import web, db
from app.core.model import Core
from app.story import Story_Page

class Story(Core):
    __tablename__ = 'story'

    active = db.Column(db.SmallInteger)
    startdate = db.Column(db.DateTime)
    enddate = db.Column(db.DateTime)
    name = db.Column(db.String(128), nullable=False)
    first_page_id = db.Column(db.Integer, db.ForeignKey('story_page.id'))

    pages = db.relationship("Story_Page", backref="story", lazy="dynamic", foreign_keys=[Story_Page.story_id])

    def is_active(self):
        return self.active and self.startdate <= datetime.now() and datetime.now() <= self.enddate
