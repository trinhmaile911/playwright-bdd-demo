from datetime import datetime, timedelta

MONTH_NAMES = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

def get_future_date(days) -> datetime:
    return datetime.today() + timedelta(days=int(days))