from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, timedelta
import json, os, uuid

APP = FastAPI(title="Mock Calendly API")

DATA_FILE = "backend/data/doctor_schedule.json"

# --- Models ---
class Patient(BaseModel):
    name: str
    email: EmailStr
    phone: str

class BookingRequest(BaseModel):
    appointment_type: str
    date: str
    start_time: str
    patient: Patient
    reason: Optional[str]

# --- Helper ---
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# --- Routes ---
@APP.get("/api/calendly/event_types")
def get_event_types():
    return [
        {"key": "consultation", "duration": 30, "name": "General Consultation"},
        {"key": "followup", "duration": 15, "name": "Follow-up"},
        {"key": "physical", "duration": 45, "name": "Physical Exam"},
        {"key": "special", "duration": 60, "name": "Specialist Consultation"}
    ]

@APP.get("/api/calendly/availability")
def get_availability(date: str, appointment_type: str):
    data = load_data()
    weekday = datetime.strptime(date, "%Y-%m-%d").strftime("%a").lower()
    hours = data["working_hours"].get(weekday, [])
    if not hours:
        return {"date": date, "available_slots": []}

    duration = {"consultation": 30, "followup": 15, "physical": 45, "special": 60}[appointment_type]
    slots = []
    for period in hours:
        start, end = period.split("-")
        start_dt = datetime.strptime(start, "%H:%M")
        end_dt = datetime.strptime(end, "%H:%M")
        while (start_dt + timedelta(minutes=duration)) <= end_dt:
            slot = {
                "start_time": start_dt.strftime("%H:%M"),
                "end_time": (start_dt + timedelta(minutes=duration)).strftime("%H:%M"),
                "available": True
            }
            slots.append(slot)
            start_dt += timedelta(minutes=duration)
    return {"date": date, "available_slots": slots}
