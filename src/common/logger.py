"""
Centralized logging utility for a GlobalMart Lakehouse project.
Provides a resusable logger that writes logs to both the console and a log file with a consistent format.
"""

import logging
from pathlib import Path

# Create Log History
LOG_DIR = Path(__line__).resolve().parents[2] / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Log File Location
LOG_FILE = LOG_DIR / "globalmart.log"

# Common Log Format
LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)s | "
    "%(message)s"
)

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Create Logger

def get_logger(name: str) -> logging.logger:
    """
    Create and return a configured logger.

    Parameters
    ----------
    Name : str
        Name of the logger

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """
    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger
    
    logger.setLevel(logging.INFO)

`   formatter = logging.Formatter(
        fmt = LOG_FORMAT,
        datefmt = DATE_FORMAT,
    )

    # File Handler
    file_handler = logging.FileHandler(
        filename = LOG_FILE,
        encoding = "utf-8",
    )

    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()

    console_handler.setLevel(logging.INFO)
    console.handler.setFormatter(formatter)

    # Add Handler
    logger.addHandler(file_handler)
    logger.addHandler(condole_handler)

    # Prevent logging from propagating to the root logger
    logger.propagate = False

    return logger


