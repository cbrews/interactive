from flask import jsonify
from app import web, db, auth
from app.story import Story, Story_Page, Story_Page_Lock, Story_Page_Content

@web.route('/story', methods=['GET'])
@auth.validate
def stories():
    return jsonify(Story.query.all())

@web.route('/story/<story_id>', methods=['GET'])
@auth.validate
def story(story_id):
    pass # Get specific story

@web.route('/story/<story_id>/start')
@auth.validate
def start_story(story_id):
    pass # Start story from the beginning

@web.route('/story/<story_id>/page/<pid>', methods=['GET'])
@auth.validate
def page(story_id, pid):
    pass # Get specific page

@web.route('/story/<story_id>/page/<pid>/unlock', methods=['POST'])
@auth.validate
def unlock(story_id, pid):
    pass # Unlock next page

'''
@app.route('/campaign')
def campaigns():
    campaigns = Campaign.query.all()

    campaign_objects = []
    for c in campaigns:
        campaign_objects.append({
            'id': c.id,
            'active': c.is_active(),
            'name': c.name,
            'first_page_id': c.first_page_id
        })

    return flask.jsonify(campaign_objects)


@app.route('/page/<id>')
def page(id):
    # Get page from database
    page = Page.query.get_or_404(id)

    # Get campaign and verify active
    campaign = page.campaign
    if not campaign.is_active():
        flask.abort(403)

    # Get access parameters in url params (ImmutableMultiDict)
    keys = flask.request.args

    # Validate locks (using param keys)
    if Access.validate(json.loads(page.locks), keys):
        return flask.jsonify({
            'next': page.next_id,
            'content': page.content
        })
    else:
        flask.abort(403)
'''
