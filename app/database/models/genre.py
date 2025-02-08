from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.database.models.base import db

genres_movies = db.Table(
    'genres_movies',
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)
)

class Genre(db.Model):

    __tablename__ = 'genres'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    movies: Mapped[list['Movie']] = relationship('Movie', secondary=genres_movies, back_populates='genres')
