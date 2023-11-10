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
