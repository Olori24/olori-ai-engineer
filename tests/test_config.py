"""
Test suite for Olori AI Engineer.
"""
from src.core.config import settings


def test_settings_load() -> None:
    """Tests that settings are loaded with default values."""
    assert settings.APP_NAME == "Olori AI Engineer"
    assert settings.LOG_LEVEL in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def test_debug_default() -> None:
    """Tests that debug is False by default."""
    assert settings.DEBUG is False
