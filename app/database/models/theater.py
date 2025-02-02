from datetime import datetime

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.database.models.base import Base


class Theater(Base):

    __tablename__ = 'theaters'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(), nullable=True)

    seats: Mapped[list['Seat']] = relationship('Seat', back_populates='theater')
    showtimes: Mapped[list['Showtime']] = relationship('Showtime', back_populates='theater')
