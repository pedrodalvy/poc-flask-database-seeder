# SQLAlchemy Model Factories POC with factory_boy

A proof-of-concept to validate the integration of `factory_boy` with SQLAlchemy for streamlined testing.  
**Key objectives**:  
- ✔️ Create reusable factories for SQLAlchemy models (including relationships).
- ✔️ Validate factory-generated data and database insertion in tests.
- ✔️ Demonstrate optional Docker/Alembic setup for extended validation.

## 🚀 Getting Started

**Prerequisites**:  
- Python 3.10+  
- Poetry (for dependency management)

**Installation**:  
```bash
poetry install
```

**Run Tests**:
```bash
poetry run pytest
```

**Optional (Docker & Alembic)**:
1. Start MySQL:
   ```bash
   docker-compose up -d
   ```  
2. Apply migrations:
   ```bash
   alembic upgrade head
   ```

## 🔍 Example Usage

**Sample Factory Usage**:
```python
# Create a User with default factory values
user = UserFactory()

# Create a Movie with explicit title and linked Genre
movie = MovieFactory(title="Inception", genre=GenreFactory(name="Sci-Fi"))
```

**Core Factories**:

| Factory              | Model       | Relationships               |
|----------------------|-------------|-----------------------------|
| `UserFactory`        | User        | -                           |
| `MovieFactory`       | Movie       | `genre` (Genre)             |
| `TheaterFactory`     | Theater     | `seats` (list of Seat)      |
| `ShowtimeFactory`    | Showtime    | `movie`, `theater`          |
| `ReservationFactory` | Reservation | `user`, `showtime`, `seats` |

## 🛠️ Additional Notes

- **Focus**: The POC centers on `factory_boy`— Docker and Alembic are optional for external DB validation.
- **Tests**:
    - A single test file (`tests/test_models.py`) validates all factories.
    - Uses an in-memory SQLite database by default.
- **Project Structure**:
    - Factories: `app/database/factories/factories.py`
    - Models: `app/database/models/*`
    - Tests: `tests/test_models.py`
