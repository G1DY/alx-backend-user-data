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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Create an instance method
        Returns
          -value (the User ID) for the key session_id in the dictionary
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ returns a User instance based on a cookie value:"""
        if not request:
            return None
        session_cookie_value = self.session_cookie(request)
        if not session_cookie_value:
            return None
        user_id = self.user_id_for_session_id(session_cookie_value)
        if not user_id:
            return None
