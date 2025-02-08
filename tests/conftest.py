from typing import Generator

import pytest
from flask import Flask
from sqlalchemy.orm import Session

from app import app
from app.database.models.base import Base
from app.database.models.base import db
from app.database.models.genre import Genre
from app.database.models.movie import Movie
from app.database.models.reservation import Reservation
from app.database.models.seat import Seat
from app.database.models.showtime import Showtime
from app.database.models.showtime_seat import ShowtimeSeat
from app.database.models.theater import Theater
from app.database.models.user import User


@pytest.fixture
def test_app() -> Flask:
    """
    Creates a test Flask application with SQLite in-memory database.
    """
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "SQLALCHEMY_ECHO": False
    })
    return app

@pytest.fixture
def test_session(test_app: Flask) -> Generator[Session, None, None]:
    """
    Provides an isolated SQLAlchemy session for testing.

    This fixture ensures each test runs with a fresh database session.
    All changes are rolled back after each test.
    """
    load_models()

    with test_app.app_context():
        db.create_all()
        session = db.session

        yield session

        session.rollback()
        session.close()
        db.drop_all()

def load_models() -> None:
    """
    Ensures all models are imported and registered with SQLAlchemy.
    """
    required_models = [Base, Genre, Movie, Showtime, ShowtimeSeat, Seat, User, Reservation, Theater]
    for _ in required_models:
        pass
