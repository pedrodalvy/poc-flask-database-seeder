from datetime import datetime, date

from sqlalchemy import String, Text, Date, DateTime, func
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.database.models.base import Base


class Movie(Base):

    __tablename__ = 'movies'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text(), nullable=False)
    poster_url: Mapped[str] = mapped_column(String(512), nullable=False)
    duration_minutes: Mapped[int] = mapped_column(SMALLINT(unsigned=True), nullable=False)
    release_date: Mapped[date] = mapped_column(Date(), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(), nullable=True)

    genres: Mapped[list['Genre']] = relationship('Genre', secondary='genres_movies', back_populates='movies')
    showtimes: Mapped[list['Showtime']] = relationship('Showtime', back_populates='movie')
