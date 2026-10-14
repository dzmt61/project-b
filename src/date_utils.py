
from datetime import date, datetime


def get_current_date() -> str:
  return date.today().isoformat()


def format_date(value: str, output_format: str = "%d.%m.%Y") -> str:
  parsed_date = datetime.strptime(value, "%Y-%m-%d")
  return parsed_date.strftime(output_format)
