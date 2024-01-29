#!/usr/bin/env python3
"""Index views module
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """
    Returns the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ 
    Returns the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def test_forbidden() -> str:
    """ 
    Returns Raise error
    """
    return abort(403)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def test_unathourized() -> str:
    """
    Returns Raise error
    """
    return abort(401)