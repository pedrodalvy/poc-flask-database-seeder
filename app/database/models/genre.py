from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.database.models.base import Base


class Genre(Base):

    __tablename__ = 'genres'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    movies: Mapped[list['Movie']] = relationship('Movie', secondary='genres_movies', back_populates='genres')
