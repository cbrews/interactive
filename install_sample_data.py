from app import web, db
from app.authentication.user import User
from app.story import Story, Story_Page, Story_Page_Lock, Story_Page_Content
from app.cryptography import random_string

admin_user = User("admin", "admin")

story = Story(active=True, name="My Test Story")

content1 = Story_Page_Content(type="Test", body="TEST")
lock1 = Story_Page_Lock(type="Test", key="PASSWORD")
page1 = Story_Page(story=story, content=content1, lock=lock1)

db.session.add(admin_user)
db.session.add(story)
db.session.add(content1)
db.session.add(lock1)
db.session.add(page1)
db.session.commit()

story.first_page_id = page1.id

db.session.add(story)
db.session.commit()
