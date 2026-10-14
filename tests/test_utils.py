
from pathlib import Path

from date_utils import get_current_date, format_date
from string_utils import reverse_string, capitalize_words
from file_utils import (
  write_text_file,
  read_text_file,
  get_file_info,
)
from logger_utils import get_logger


def test_date_utils():
  assert len(get_current_date()) == 10
  assert format_date("2026-10-14") == "14.10.2026"


def test_string_utils():
  assert reverse_string("hello") == "olleh"
  assert capitalize_words("hello world") == "Hello World"


def test_file_utils(tmp_path):
  file_path = tmp_path / "example.txt"

  write_text_file(str(file_path), "Тестовый текст")

  assert read_text_file(str(file_path)) == "Тестовый текст"

  info = get_file_info(str(file_path))
  assert info["name"] == "example.txt"
  assert info["extension"] == ".txt"
  assert info["size"] > 0


def test_logger_utils(tmp_path):
  log_path = tmp_path / "test.log"
  logger = get_logger(
    name=f"test_logger_{log_path.name}",
    log_file=str(log_path),
  )

  logger.info("Integration test")

  for handler in logger.handlers:
    handler.flush()

  assert log_path.exists()
  assert "Integration test" in log_path.read_text(
    encoding="utf-8"
  )
