#!/usr/bin/env python3
"""flask app"""
from flask import Flask, jsonify, request, abort, redirect
from flask.helpers import make_response
from db import DB
from user import User
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def get_payload():
    payload = {"message": "Bienvenue"}
    return jsonify(payload)


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """end-point to register a user"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """login function to respond to the POST /sessions route."""
    user_request = request.form
    user_email = user_request.get('email', '')
    user_password = user_request.get('password', '')
    valid_log = AUTH.valid_login(user_email, user_password)
    if not valid_log:
        abort(401)
    response = make_response(jsonify({"email": user_email,
                                      "message": "logged in"}))
    response.set_cookie('session_id', AUTH.create_session(user_email))
    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """logout a logged in user and destrys their session"""
    session_id = request.cookies.get("session_id", None)
    if not session_id:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        response = redirect('/')
        response.delete_cookie('session_id')
        return response
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """returns user profile or 403 if the user is invalid"""
    session_id = request.cookies.get("session_id", None)
    if not session_id:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user})
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """returns reset password token"""
    user_request = request.form
    user_email = user_request.get('email', '')
    registered_emails = AUTH.create_session(user_email)
    if not registered_emails:
        abort(403)
    reset_token = AUTH.get_reset_password_token(user_email)
    return jsonify({"email": user_email, "reset_token": reset_token}), 200


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """updates a password to a new one"""
    user_email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')
    if not reset_token:
        abort(403)
    try:
        AUTH.update_password(reset_token, new_password)
    except Exception:
        abort(403)
    return jsonify({"email": user_email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
