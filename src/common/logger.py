"""
Project     : GlobalMart Enterprise Lakehouse
Module      : Centralized Logger
Author      : Ambuj Kumar
Description : Provides a centralized logging utility for the GlobalMart
              Enterprise Lakehouse project.

Features
--------
- Console logging
- File logging
- Consistent log formatting
- Reusable logger instances
- Duplicate handler prevention
"""

from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler

# ==========================================================
# Constants
# ==========================================================

LOG_DIRECTORY = "logs"
LOG_FILE_NAME = "globalmart.log"
DEFAULT_LOG_LEVEL = logging.INFO
LOG_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
LOG_BACKUP_COUNT = 5

LOG_DIR = Path(__file__).resolve().parents[2] / LOG_DIRECTORY
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / LOG_FILE_NAME

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)s | "
    "%(message)s"
)

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


# ==========================================================
# Logger Factory
# ==========================================================

def get_logger(name: str) -> logging.Logger:
    """
    Create and return a configured logger.

    Parameters
    ----------
    name : str
        Name of the logger.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(DEFAULT_LOG_LEVEL)

    formatter = logging.Formatter(
        fmt=LOG_FORMAT,
        datefmt=DATE_FORMAT,
    )

    # ======================================================
    # File Handler
    # ======================================================

    file_handler = RotatingFileHandler(
        filename=LOG_FILE,
        maxBytes=LOG_FILE_SIZE,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )

    file_handler.setLevel(DEFAULT_LOG_LEVEL)
    file_handler.setFormatter(formatter)

    # ======================================================
    # Console Handler
    # ======================================================

    console_handler = logging.StreamHandler()

    console_handler.setLevel(DEFAULT_LOG_LEVEL)
    console_handler.setFormatter(formatter)

    # ======================================================
    # Register Handlers
    # ======================================================

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Prevent duplicate logging
    logger.propagate = False

    return logger


__all__ = ["get_logger"]