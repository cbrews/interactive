from flask import jsonify, abort, request
from app import web, db, auth
from app.story import Story, Story_Page, Story_Page_Lock, Story_Page_Content
from pprint import pprint

@web.route('/story', methods=['GET'])
@auth.validate
def stories():
    stories = Story.query.all()

    return jsonify(map(lambda s: {
        'id': s.id,
        'active': s.is_active(),
        'name': s.name
    }, stories))

@web.route('/story/<story_id>', methods=['GET'])
@auth.validate
def story(story_id):
    story = Story.query.get(story_id)

    authenticateStory(story)

    return jsonify({
        'id': story.id,
        'active': story.is_active(),
        'startdate': story.startdate,
        'enddate': story.enddate,
        'name': story.name
    })

@web.route('/story/<story_id>/start', methods=["POST"])
@auth.validate
def start_story(story_id):
    story = Story.query.get(story_id)

    authenticateStory(story)

    if not story.first_page:
        print "No first page was found for story ${story.id}"
        abort(501)

    return jsonify({
        'page': story.first_page.hash,
        'page_token': story.first_page.getSignedToken(auth.getToken())
    })


@web.route('/story/<story_id>/page/<pid>', methods=['GET'])
@auth.validate
def page(story_id, pid):
    page = Story_Page.query.filter_by(hash=pid).first()

    authenticatePage(page, story_id)

    return jsonify({
        "id": page.hash,
        "body_type": page.content.type,
        "body": page.content.body,
        "additional_data": page.content.additional_data,
        "lock_type": page.lock.type
    })

@web.route('/story/<story_id>/page/<pid>/unlock', methods=['POST'])
@auth.validate
def unlock(story_id, pid):
    page = Story_Page.query.filter_by(hash=pid).first()

    authenticatePage(page, story_id)

    return jsonify({
        "unlocked": True
    })

def authenticatePage(page, story_id):

    if not page or page.story.id != int(story_id):
        abort(404)

    authenticateStory(page.story)

    token = ""
    if "x-page-token" in request.headers:
        token = request.headers['x-page-token']

    if not page.authenticateHash(token):
        abort(401)

    return True

def authenticateStory(story):
    if not story:
        abort(404)

    if not story.is_active():
        abort(403)

    return True
