from backend.app.schemas.booking import BookingRequest
import pytest
from pydantic import ValidationError


def test_valid_booking():
    booking = BookingRequest(
        customer_name="John Doe",
        phone_number="1234567890",
        guest_count=4
    )
    assert booking.customer_name == "John Doe"
    assert booking.phone_number == "1234567890"
    assert booking.guest_count == 4

def test_invalid_guest_count():
    with pytest.raises(ValidationError):
        BookingRequest(
            customer_name="Jane Doe",
            phone_number="0987654321",
            guest_count=25  # Invalid guest count
        )

def test_mobile_number_format():
    with pytest.raises(ValidationError):
        BookingRequest(
            customer_name="Alice Smith",
            phone_number="12345",  # Invalid phone number format
            guest_count=2
        )

def test_empty_customer_name():
    with pytest.raises(ValidationError):
        BookingRequest(
            customer_name="",  # Empty customer name
            phone_number="1234567890",
            guest_count=3
        )