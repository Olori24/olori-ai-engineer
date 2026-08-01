"""
Main entry point for Olori AI Engineer.
Orchestrates application startup and execution.
"""
import logging
import sys

from src.core.config import settings
from src.core.exceptions import OloriError
from src.core.logging import setup_logging


def main() -> None:
    """
    Main execution loop.
    """
    # 1. Initialize Logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    logger.info("Starting %s...", settings.APP_NAME)
    
    try:
        # 2. Run Application Logic (Placeholder)
        logger.debug("Debug mode is %s", "ENABLED" if settings.DEBUG else "DISABLED")
        
        # Simulating work
        print(f"Hello from {settings.APP_NAME}!")
        
    except OloriError as e:
        logger.error("Application error: %s", e)
        sys.exit(1)
    except Exception as e:
        logger.critical("Unexpected error: %s", e, exc_info=True)
        sys.exit(1)
    finally:
        logger.info("Shutting down %s.", settings.APP_NAME)


if __name__ == "__main__":
    main()
