from datetime import timedelta

from factory import Faker, LazyAttribute, SubFactory
from factory.alchemy import SQLAlchemyModelFactory

from app.database.models.base import db
from app.database.models.genre import Genre
from app.database.models.movie import Movie
from app.database.models.reservation import Reservation
from app.database.models.seat import Seat
from app.database.models.showtime import Showtime
from app.database.models.showtime_seat import ShowtimeSeat
from app.database.models.theater import Theater
from app.database.models.user import User
from app.enums.reservation_status import ReservationStatus
from app.enums.showtime_seat_status import ShowtimeSeatStatus
from app.enums.user_roles import UserRoles


class GenreFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Genre
        sqlalchemy_session = db.session

    name = Faker('word')


class MovieFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Movie
        sqlalchemy_session = db.session

    title = Faker('sentence')
    description = Faker('text')
    poster_url = Faker('url')
    duration_minutes = Faker('random_int', min=60, max=200)
    release_date = Faker('date_object')


class TheaterFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Theater
        sqlalchemy_session = db.session

    name = Faker('word')
    location = Faker('address')


class ShowtimeFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Showtime
        sqlalchemy_session = db.session

    start_time = Faker('date_time')
    end_time = LazyAttribute(lambda o: o.start_time + timedelta(minutes=o.movie.duration_minutes))
    movie = SubFactory(MovieFactory)
    theater = SubFactory(TheaterFactory)

class SeatFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Seat
        sqlalchemy_session = db.session

    row = Faker('word')
    number = Faker('random_int', min=1, max=100)
    price = Faker('random_int', min=1, max=100)
    theater = SubFactory(TheaterFactory)


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    email = Faker('email')
    role = UserRoles.USER

class ReservationFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Reservation
        sqlalchemy_session = db.session

    status = ReservationStatus.CONFIRMED
    reservation_time = Faker('date_time')
    showtime = SubFactory(ShowtimeFactory)
    seat = SubFactory(SeatFactory)
    user = SubFactory(UserFactory)


class ShowtimeSeatFactory(SQLAlchemyModelFactory):
    class Meta:
        model = ShowtimeSeat
        sqlalchemy_session = db.session

    status = ShowtimeSeatStatus.AVAILABLE
    price = Faker('random_int', min=1, max=100)
    reservation = SubFactory(ReservationFactory)
    seat = SubFactory(SeatFactory)
    showtime = SubFactory(ShowtimeFactory)
