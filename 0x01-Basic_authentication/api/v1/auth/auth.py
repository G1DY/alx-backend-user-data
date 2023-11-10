#!/usr/bin/env python3
"""a class to manage the API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """manages API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False - path and excluded_paths"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        # make sure all paths end with a slash for comparison
        path = path.rstrip("/") + "/"
        excluded_paths = [p.rstrip("/") + "/" for p in excluded_paths]

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """returns None - request will be the Flask request object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request will be the Flask request object"""
        return None
