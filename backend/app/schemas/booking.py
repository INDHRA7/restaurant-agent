from pydantic import BaseModel , Field
class BookingRequest(BaseModel):
    customer_name : str = Field(min_length=1)
    phone_number : str = Field(min_length=1,
                               max_length=10,
                               pattern=r"^\d{10}$")
    guest_count : int = Field(ge=1,le = 20)

