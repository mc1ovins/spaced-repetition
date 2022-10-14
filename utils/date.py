from datetime import date


def days_elapsed(d1: date, d2: date) -> int:
    """Return the number of days elapsed since the given date."""
    return (d1 - d2).days
