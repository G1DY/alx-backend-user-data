#!/usr/bin/env python3
"""Implements a hash_password function that expects one string
   argument name password and returns a salted
"""
def hash_password(password: str) -> bytes:
    """hashing function"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
