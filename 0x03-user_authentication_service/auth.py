#!/usr/bin/env python3
"""hash password module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> str:
    """takes in a password string arguments and returns bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """generates new uuid"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registers user_email and user_password under object User"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists.".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """validates email and password and return a boolean"""
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
        except NoResultFound:
            pass
        return False

    def create_session(self, email: str) -> str:
        """It takes an email string argument
            -returns the session ID as a string
        """
        session_id = _generate_uuid()
        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
