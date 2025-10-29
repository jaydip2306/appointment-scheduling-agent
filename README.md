# Lyzr Scheduling Agent - Mock Calendly Integration

## Quickstart

1. Create & activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run the API

```bash
python run.py
```

3. Test endpoints

```bash
curl "http://localhost:8000/api/calendly/availability?date=2025-10-30&appointment_type=consultation"
```
