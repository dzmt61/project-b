from datetime import date


def get_current_date():
  return date.today().isoformat()


def format_date(value):
  if isinstance(value, date):
    return value.strftime("%d.%m.%Y")

  raise TypeError("value must be a date object")