#!/usr/bin/env python3
"""module to Create a new Flask view that handles
   all routes for the Session authentication.
"""
from api.v1.views import app_views
from models.user import User
from os import getenv, abort, environ
from flask import jsonify, request


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """handles user authetication using Session ID"""
    user_email = request.form.get('user_email')
    user_password = request.form.get('user_password')

    if not user_email:
        return jsonify({"error": "email missing"}), 400
    if not user_password:
        return jsonify({"error": "password missing"}), 400
    user = User.search({'user_email': email})
    if not user:
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
