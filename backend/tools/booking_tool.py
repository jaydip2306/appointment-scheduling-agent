import httpx
from typing import Any

BASE = "http://localhost:8000/api/calendly"

async def create_booking(payload: dict) -> Any:
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{BASE}/book", json=payload)
        r.raise_for_status()
        return r.json()
