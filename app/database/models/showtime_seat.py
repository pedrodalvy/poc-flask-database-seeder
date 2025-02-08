from sqlalchemy import Enum, DECIMAL, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.database.models.base import db
from app.enums.showtime_seat_status import ShowtimeSeatStatus


class ShowtimeSeat(db.Model):

    __tablename__ = 'showtime_seats'

    id: Mapped[int] = mapped_column(primary_key=True)
    showtime_id: Mapped[int] = mapped_column(ForeignKey('showtimes.id'))
    seat_id: Mapped[int] = mapped_column(ForeignKey('seats.id'))
    reservation_id: Mapped[int] = mapped_column(ForeignKey('reservations.id'))
    status: Mapped[ShowtimeSeatStatus] = mapped_column(Enum(ShowtimeSeatStatus), nullable=False)
    price: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)

    showtime: Mapped['Showtime'] = relationship('Showtime', back_populates='showtime_seats')
    seat: Mapped['Seat'] = relationship('Seat', back_populates='showtime_seats')
    reservation: Mapped['Reservation'] = relationship('Reservation', back_populates='showtime_seats')
