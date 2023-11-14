#!/usr/bin/env python3
"""flask app"""
from flask import Flask, jsonify, request, abort
from flask.helpers import make_response
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
    valid_login = AUTH.valid_login(user_email, user_password)
    if not valid_login:
        abort(401)
    response = make_response(jsonify({"email": user_email,
                                      "message": "looged in"}))
    response.set_cookie('session_id', AUTH.create_session(user_email))
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
