"""
Custom exceptions for Olori AI Engineer.
"""

class OloriError(Exception):
    """Base exception for all application errors."""
    pass


class ConfigurationError(OloriError):
    """Raised when there is an issue with application configuration."""
    pass


class ServiceError(OloriError):
    """Raised when a service operation fails."""
    pass
