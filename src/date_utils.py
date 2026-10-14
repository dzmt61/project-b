from datetime import date


def get_current_date():
  return date.today().strftime("%d.%m.%Y")

def format_date(value):
  if isinstance(value, date):
    return value.strftime("%d.%m.%Y")

  raise TypeError("value must be a date object")

def is_weekend(value):
  return value.weekday() >= 5