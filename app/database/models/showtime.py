from datetime import datetime

from sqlalchemy import DateTime, func, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.database.models.base import db


class Showtime(db.Model):

    __tablename__ = 'showtimes'

    id: Mapped[int] = mapped_column(primary_key=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey('movies.id'))
    theater_id: Mapped[int] = mapped_column(ForeignKey('theaters.id'))
    start_time: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(), nullable=True)

    movie: Mapped['Movie'] = relationship('Movie', back_populates='showtimes')
    theater: Mapped['Theater'] = relationship('Theater', back_populates='showtimes')
    reservations: Mapped[list['Reservation']] = relationship('Reservation', back_populates='showtime')
    showtime_seats: Mapped[list['ShowtimeSeat']] = relationship('ShowtimeSeat', back_populates='showtime')
