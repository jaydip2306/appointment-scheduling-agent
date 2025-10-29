from datetime import datetime

def parse_date(text: str) -> str:
    try:
        dt = datetime.fromisoformat(text)
        return dt.date().isoformat()
    except Exception:
        raise ValueError('Unsupported date format; use YYYY-MM-DD')
