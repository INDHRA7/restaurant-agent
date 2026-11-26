from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException

from backend.app.schemas.booking import BookingRequest
from backend.app.models.booking import Booking
from database.session import get_db

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.post("/")
def create_booking(
    booking: BookingRequest,
    db: Session = Depends(get_db)
):
    new_booking = Booking(
        customer_name=booking.customer_name,
        phone_number=booking.phone_number,
        guest_count=booking.guest_count
    )

    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)

    return {
        "message": "Booking created successfully",
        "booking": new_booking
    }
@router.get("/")
def get_booking(
        db: Session = Depends(get_db)
):
    bookings = db.query(Booking).all()
    return {
        "message": "Bookings retrieved successfully",
        "bookings": bookings
    }

from fastapi import HTTPException

@router.get("/{booking_id}")
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking

@router.put("/{booking_id}")
def update_booking(
    booking_id: int,
    booking_data: BookingRequest,
    db: Session = Depends(get_db)
):
    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    booking.customer_name = booking_data.customer_name
    booking.phone_number = booking_data.phone_number
    booking.guest_count = booking_data.guest_count

    db.commit()
    db.refresh(booking)

    return {
        "message": "Booking updated successfully",
        "booking": booking
    }

@router.delete("/{booking_id}")
def delete_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):
    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    db.delete(booking)
    db.commit()

    return {
        "message": "Booking deleted successfully"
    }