#!/usr/bin/env python3
"""a class BasicAuth that inherits from Auth"""
from api.v1.auth.auth import Auth
from base64 import b64decode, decode
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """inherits from Auth"""
    def extract_base64_authorization_header(self, auth_header: str) -> str:
        """returns the Base64 part of the Authorization header"""
        if auth_header is None or not isinstance(auth_header, str):
            return None
        if not auth_header.startswith("Basic "):
            return None
        return auth_header.split(" ")[1]

    def decode_base64_authorization_header(self, b64_auth_header: str) -> str:
        """returns the decoded Base64 string base64_authorization_header"""
        if b64_auth_header is None or not isinstance(b64_auth_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(b64_auth_header)
        except base64.binascii.Error:
            return None
        return decoded_bytes.decode('utf-8')

    def extract_user_credentials(
            self, decoded_b64_auth_header: str) -> (str, str):
        """returns the user email and password from the Base64 decoded value"""
        if decoded_b64_auth_header is None or not isinstance(
                decoded_b64_auth_header, str) \
           or ':' not in decoded_b64_auth_header:
            return (None, None)
        return decoded_b64_auth_header.split(':', 1)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if user_email is None or not isinstance(
                user_email, str) or user_pwd is None or not isinstance(
                     user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request"""
        auth_header = self.authorization_header(request)
        if not auth_header:
            return None
        extract_base64 = self.extract_base64_authorization_header(auth_header)
        if extract_base64 is None:
            return None
        decode_base64 = self.decode_base64_authorization_header(extract_base64)
        if decode_base64 is None:
            return None
        user_credentials = self.extract_user_credentials(decode_base64)
        if user_credentials is None or len(user_credentials) != 2:
            return None
        user_email, user_password = user_credetials
        user_instance = self.user_object_from_credentials(
                user_email, user_password)
        return user_instance
