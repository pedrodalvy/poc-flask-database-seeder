"""
Base model class to be inherited by other SQLAlchemy models
"""
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base model class
    """
