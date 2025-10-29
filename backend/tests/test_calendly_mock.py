import pytest
from fastapi.testclient import TestClient
from backend.api.calendly_mock import APP

client = TestClient(APP)

def test_event_types():
    r = client.get('/api/calendly/event_types')
    assert r.status_code == 200
    assert any(e['key']=='consultation' for e in r.json())

def test_availability_and_booking_flow():
    r = client.get('/api/calendly/availability', params={'date':'2025-10-30','appointment_type':'consultation'})
    assert r.status_code == 200
    payload = {
        "appointment_type": "consultation",
        "date": "2025-10-31",
        "start_time": "09:00",
        "patient": {"name":"PyTest", "email":"p@test.com", "phone":"+911234"},
        "reason": "Testing"
    }
    rb = client.post('/api/calendly/book', json=payload)
    assert rb.status_code in (200,201)
    data = rb.json()
    assert 'booking_id' in data
