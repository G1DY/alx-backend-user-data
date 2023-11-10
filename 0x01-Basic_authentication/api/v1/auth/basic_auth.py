#!/usr/bin/env python3
"""a class BasicAuth that inherits from Auth"""
from api.v1.auth.auth import Auth
from base64 import b64decode, decode
import base64


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
