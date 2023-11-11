#!/usr/bin/env python3
"""module with class SessionAuth"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """class SessionAuth that inherits from Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id
        Returns:
          -Return None if user_id is None
          -Return None if user_id is not a string
          -Generate a Session ID using uuid module and uuid4() like id in Base
          -Use this Session ID as key of the dictionary user_id_by_session_id
          -Return the Session ID
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
