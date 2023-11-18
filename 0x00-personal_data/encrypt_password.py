#!/usr/bin/env python3
"""Implements a hash_password function that expects one string
   argument name password and returns a salted
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hashing function"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validates hashed password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
