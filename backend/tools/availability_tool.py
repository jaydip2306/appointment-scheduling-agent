import httpx
from typing import Any

BASE = "http://localhost:8000/api/calendly"

async def fetch_availability(date: str, appointment_type: str) -> Any:
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{BASE}/availability", params={"date": date, "appointment_type": appointment_type})
        r.raise_for_status()
        return r.json()
