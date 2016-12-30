import flask
import app.access as Access
import json
from app import app, db
from models import Page, Campaign

@app.errorhandler(404)
def no_route(e):
    return flask.jsonify({'error': 'Page Not Found'}), 404

@app.errorhandler(403)
def no_auth(e):
    return flask.jsonify({'error': 'Not Authorized'}), 403

'''
Frontend facing routes
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