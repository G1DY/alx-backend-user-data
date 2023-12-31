#!/usr/bin/env python3
"""module to Create a new Flask view that handles
   all routes for the Session authentication.
"""
from api.v1.views import app_views
from models.user import User
from os import getenv, abort, environ
from flask import jsonify, request
from werkzeug import exceptions


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """handles user authetication using Session ID"""
    user_email = request.form.get('email')
    user_password = request.form.get('password')

    if not user_email:
        return jsonify({"error": "email missing"}), 400
    if not user_password:
        return jsonify({"error": "password missing"}), 400

    is_valid_user = User.search({'email': user_email})
    if not is_valid_user:
        return jsonify({"error": "no user found for this email"}), 404

    is_valid_user = is_valid_user[0]
    if not is_valid_user.is_valid_password(user_password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(is_valid_user.id)
    cookie_response = getenv('SESSION_NAME')
    user_dict = jsonify(is_valid_user.to_json())

    user_dict.set_cookie(cookie_response, session_id)
    return user_dict


@app_views.route(
    '/auth_session/logout',
    methods=['DELETE'],
    strict_slashes=False)
def session_logout() -> str:
    """DELETE /api/v1/auth_session/logout"""
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
