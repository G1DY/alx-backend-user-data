#!/usr/bin/env python3
"""module that creates SQLAlchemy model named User
   for a database table named users
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """class with database table named users"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(150), nullable=False)
    hashed_password = Column(String(150), nullable=True)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
