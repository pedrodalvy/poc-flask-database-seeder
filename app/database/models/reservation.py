from datetime import datetime

from sqlalchemy import DateTime, func, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base import db
from app.enums.reservation_status import ReservationStatus


class Reservation(db.Model):

    __tablename__ = 'reservations'

    id: Mapped[int] = mapped_column(primary_key=True)
    showtime_id: Mapped[int] = mapped_column(ForeignKey('showtimes.id'))
    seat_id: Mapped[int] = mapped_column(ForeignKey('seats.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    reservation_time: Mapped[datetime] = mapped_column(DateTime(), nullable=False, server_default=func.now())
    status: Mapped[ReservationStatus] = mapped_column(Enum(ReservationStatus), nullable=False)

    showtime: Mapped['Showtime'] = relationship('Showtime', back_populates='reservations')
    seat: Mapped['Seat'] = relationship('Seat', back_populates='reservations')
    user: Mapped['User'] = relationship('User', back_populates='reservations')
    showtime_seats: Mapped[list['ShowtimeSeat']] = relationship('ShowtimeSeat', back_populates='reservation')
