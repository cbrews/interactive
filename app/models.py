from app import db
from datetime import datetime

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.SmallInteger)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    first_page_id = db.Column(db.Integer) # Reference to first page, keeping it decoupled for now
    author = db.Column(db.String(128))

    pages = db.relationship("Page", backref="campaign", lazy="dynamic")

    def is_active(self):
        return self.active and self.start <= datetime.now() and datetime.now() <= self.end

class Page(db.Model):
    id = db.Column(db.String(128), primary_key=True)
    next_id = db.Column(db.String(128), db.ForeignKey('page.id'))
    content = db.Column(db.String(256))
    locks = db.Column(db.String(512), nullable=False)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)