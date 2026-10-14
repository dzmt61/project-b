import logging
from pathlib import Path


def get_logger(
  name: str = "project_a",
  log_file: str = "logs/app.log",
) -> logging.Logger:

  logger = logging.getLogger(name)
  logger.setLevel(logging.INFO)
  logger.propagate = False

  if not logger.handlers:
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    handler = logging.FileHandler(
      log_path,
      encoding="utf-8",
    )
    handler.setFormatter(
      logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
      )
    )

    logger.addHandler(handler)

  return logger
