from sqlalchemy.orm import Session

from app.database.factories.facories import GenreFactory, MovieFactory, TheaterFactory, ShowtimeFactory, SeatFactory, UserFactory, ReservationFactory, ShowtimeSeatFactory
from app.database.models.genre import Genre
from app.database.models.movie import Movie
from app.database.models.reservation import Reservation
from app.database.models.seat import Seat
from app.database.models.showtime import Showtime
from app.database.models.showtime_seat import ShowtimeSeat
from app.database.models.theater import Theater
from app.database.models.user import User


def test_create_genre(test_session: Session):
    # Arrange
    genre = GenreFactory.create()

    # Act
    genre_from_db = test_session.query(Genre).first()

    # Assert
    assert genre.id == genre_from_db.id
    assert genre.name == genre_from_db.name

def test_create_movie(test_session: Session):
    # Arrange
    movie = MovieFactory.create()

    # Act
    movie_from_db = test_session.query(Movie).first()

    # Assert
    assert movie.id == movie_from_db.id
    assert movie.title == movie_from_db.title
    assert movie.description == movie_from_db.description
    assert movie.poster_url == movie_from_db.poster_url
    assert movie.duration_minutes == movie_from_db.duration_minutes
    assert movie.release_date == movie_from_db.release_date
    assert len(movie.genres) == 0

def test_create_movie_with_genres(test_session: Session):
    # Arrange
    movie = MovieFactory.create(genres=[GenreFactory()])

    # Act
    movie_from_db = test_session.query(Movie).first()

    # Assert
    assert len(movie.genres) == 1
    assert movie.genres[0].id == movie_from_db.genres[0].id

def test_create_theater(test_session: Session):
    # Arrange
    theater = TheaterFactory.create()

    # Act
    theater_from_db = test_session.query(Theater).first()

    # Assert
    assert theater.id == theater_from_db.id
    assert theater.name == theater_from_db.name
    assert theater.location == theater_from_db.location
    assert theater.created_at is not None



def test_create_showtime(test_session: Session):
    # Arrange
    movie = MovieFactory.create()
    theater = TheaterFactory.create()
    showtime = ShowtimeFactory.create(movie=movie, theater=theater)

    # Act
    showtime_from_db = test_session.query(Showtime).first()

    # Assert
    assert showtime.id == showtime_from_db.id
    assert showtime.movie_id == showtime_from_db.movie_id
    assert showtime.theater_id == showtime_from_db.theater_id


def test_create_seat(test_session: Session):
    # Arrange
    theater = TheaterFactory.create()
    seats = SeatFactory.create_batch(theater=theater, size=3)

    # Act
    seats_from_db = test_session.query(Seat).all()

    # Assert
    assert len(seats) == len(seats_from_db)
    assert len(seats_from_db) == 3

    for seat, seat_from_db in zip(seats, seats_from_db):
        assert seat.id == seat_from_db.id
        assert seat.theater_id == seat_from_db.theater_id
        assert seat.row == seat_from_db.row
        assert seat.number == seat_from_db.number
        assert seat.price == seat_from_db.price

def test_create_user(test_session: Session):
    # Arrange
    user = UserFactory.create()

    # Act
    user_from_db = test_session.query(User).first()

    # Assert
    assert user.id == user_from_db.id
    assert user.email == user_from_db.email

def test_create_reservation(test_session: Session):
    # Arrange
    showtime = ShowtimeFactory.create()
    seat = SeatFactory.create()
    user = UserFactory.create()

    reservation = ReservationFactory.create(showtime=showtime, seat=seat, user=user)

    # Act
    reservation_from_db = test_session.query(Reservation).first()

    # Assert
    assert reservation.id == reservation_from_db.id
    assert reservation.showtime_id == reservation_from_db.showtime_id
    assert reservation.seat_id == reservation_from_db.seat_id
    assert reservation.user_id == reservation_from_db.user_id


def test_create_showtime_seat(test_session: Session):
    # Arrange
    showtime_seat = ShowtimeSeatFactory.create()

    # Act
    showtime_seat_from_db = test_session.query(ShowtimeSeat).first()

    # Assert
    assert showtime_seat.id == showtime_seat_from_db.id
    assert showtime_seat.showtime_id == showtime_seat_from_db.showtime_id
    assert showtime_seat.seat_id == showtime_seat_from_db.seat_id

def test_test_create_showtime_seat_without_reservation(test_session: Session):
    # Arrange
    showtime_seat = ShowtimeSeatFactory.create(reservation=None)

    # Act
    showtime_seat_from_db = test_session.query(ShowtimeSeat).first()

    # Assert
    assert showtime_seat_from_db.id == showtime_seat.id
    assert showtime_seat.reservation_id is None
    assert showtime_seat_from_db.reservation_id is None
