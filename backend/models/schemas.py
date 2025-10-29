from pydantic import BaseModel, EmailStr
from typing import Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    phone: str

class BookingRequest(BaseModel):
    appointment_type: str
    date: str
    start_time: str
    patient: Patient
    reason: Optional[str] = None

class BookingResponse(BaseModel):
    booking_id: str
    status: str
    confirmation_code: str
    details: dict

class AvailabilitySlot(BaseModel):
    start_time: str
    end_time: str
    available: bool

class AvailabilityResponse(BaseModel):
    date: str
    available_slots: list[AvailabilitySlot]
