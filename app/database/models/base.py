"""
Base model class to be inherited by other SQLAlchemy models
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base model class
    """

db = SQLAlchemy(model_class=Base)
