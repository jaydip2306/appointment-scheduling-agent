from fastapi import FastAPI
from .calendly_mock import APP as calendly_app

app = FastAPI(title="Lyzr Scheduling Agent Backend")

@app.get("/")
def root():
    return {
        "message": "Calendly Mock API is running ✅",
        "available_routes": [
            "/healthz",
            "/calendly/api/calendly/event_types",
            "/calendly/\api/calendly/availability?date=2025-10-30&appointment_type=consultation",
        
        ]
    }

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

# ✅ Mount calendly_app under /calendly
app.mount("/calendly", calendly_app)
