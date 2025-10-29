import asyncio
from typing import List
from ..tools.availability_tool import fetch_availability
from ..tools.booking_tool import create_booking

async def recommend_slots(date: str, appointment_type: str) -> List[dict]:
    data = await fetch_availability(date, appointment_type)
    slots = [s for s in data.get('available_slots', []) if s['available']]
    return slots[:3]

async def book_slot(date: str, start_time: str, appointment_type: str, patient: dict, reason: str):
    payload = {
        "appointment_type": appointment_type,
        "date": date,
        "start_time": start_time,
        "patient": patient,
        "reason": reason,
    }
    return await create_booking(payload)

if __name__ == '__main__':
    async def demo():
        rec = await recommend_slots('2025-10-30', 'consultation')
        print('Recommended:', rec)
    asyncio.run(demo())
