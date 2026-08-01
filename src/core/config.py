"""
Configuration management for Olori AI Engineer.
Mocked for environments without Pydantic.
"""
from pathlib import Path
from typing import Literal

class Settings:
    """
    Mocked application settings.
    """
    APP_NAME: str = "Olori AI Engineer"
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    LOG_FILE: Path = Path("logs/app.log")
    OPENAI_API_KEY: str | None = None
    ANTHROPIC_API_KEY: str | None = None

settings = Settings()
