from datetime import date

from sqlalchemy.orm import Session

from app.database.models.genre import Genre
from app.database.models.movie import Movie


def test_create_genre(test_session: Session):
    # Arrange
    genre = Genre(name='Drama')

    # Act
    test_session.add(genre)
    test_session.commit()
    genre_from_db = test_session.query(Genre).first()

    # Assert
    assert genre.id == genre_from_db.id
    assert genre.name == genre_from_db.name

def test_create_movie(test_session: Session):
    # Arrange
    genre = Genre(name='Drama')
    movie = Movie(
        title='Interstellar',
        description="A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        poster_url='https://foo.com/bar.jpg',
        duration_minutes=120,
        release_date=date(1994, 9, 22),
        genres=[genre]
    )

    # Act
    test_session.add(movie)
    test_session.commit()
    movie_from_db = test_session.query(Movie).first()

    # Assert
    assert movie.id == movie_from_db.id
    assert movie.title == movie_from_db.title
    assert movie.description == movie_from_db.description
    assert movie.poster_url == movie_from_db.poster_url
    assert movie.duration_minutes == movie_from_db.duration_minutes
    assert movie.release_date == movie_from_db.release_date
    assert movie.genres[0].id == movie_from_db.genres[0].id
