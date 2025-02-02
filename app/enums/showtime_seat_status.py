from enum import Enum


class ShowtimeSeatStatus(Enum):
    AVAILABLE = 'available'
    RESERVED = 'reserved'
    CANCELLED = 'cancelled'
