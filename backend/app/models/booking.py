from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from backend.app.database.base import Base

class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    customer_name: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(10))
    guest_count: Mapped[int] = mapped_column(Integer)

