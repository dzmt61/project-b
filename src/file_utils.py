from pathlib import Path


def write_text_file(path: str, content: str) -> str:
  file_path = Path(path)
  file_path.parent.mkdir(parents=True, exist_ok=True)
  file_path.write_text(content, encoding="utf-8")
  return str(file_path)


def read_text_file(path: str) -> str:
  return Path(path).read_text(encoding="utf-8")


def get_file_info(path: str) -> dict:
  file_path = Path(path)

  if not file_path.is_file():
    raise FileNotFoundError(f"Файл не найден: {path}")

  return {
    "name": file_path.name,
    "size": file_path.stat().st_size,
    "extension": file_path.suffix,
  }
