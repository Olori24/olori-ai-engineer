"""
Logging configuration for Olori AI Engineer.
Provides both console and file handlers with structured formatting.
"""
import logging
import sys
from pathlib import Path

from src.core.config import settings


def setup_logging() -> None:
    """
    Configures the global logging system.
    Creates log directories if they don't exist.
    """
    # Ensure log directory exists
    settings.LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Define formatting
    log_format = (
        "%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d - %(message)s"
    )
    date_format = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(log_format, datefmt=date_format)

    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(settings.LOG_LEVEL)

    # Clear existing handlers
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # File Handler
    file_handler = logging.FileHandler(settings.LOG_FILE)
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)

    logging.info("Logging initialized with level: %s", settings.LOG_LEVEL)
