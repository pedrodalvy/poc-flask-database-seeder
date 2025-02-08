from datetime import datetime

from sqlalchemy import String, DECIMAL, DateTime, func, ForeignKey
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base import db


class Seat(db.Model):

    __tablename__ = 'seats'

    id: Mapped[int] = mapped_column(primary_key=True)
    theater_id: Mapped[int] = mapped_column(ForeignKey('theaters.id'))
    row: Mapped[str] = mapped_column(String(5), nullable=False)
    number: Mapped[int] = mapped_column(SMALLINT(unsigned=True), nullable=False)
    price: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(), nullable=True)

    theater: Mapped['Theater'] = relationship('Theater', back_populates='seats')
    reservations: Mapped[list['Reservation']] = relationship('Reservation', back_populates='seat')
    showtime_seats: Mapped[list['ShowtimeSeat']] = relationship('ShowtimeSeat', back_populates='seat')
