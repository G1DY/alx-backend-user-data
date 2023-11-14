#!/usr/bin/env python3
"""hash password module
"""
import bcrypt


def _hash_password(password: str) -> str:
    """takes in a password string arguments and returns bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
