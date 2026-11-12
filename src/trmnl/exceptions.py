"""Asynchronous Python client for TRMNL."""


class TRMNLError(Exception):
    """Generic exception."""


class TRMNLAuthenticationError(TRMNLError):
    """Authentication error."""


class TRMNLForbiddenError(TRMNLError):
    """The API key may not reach this resource."""


class TRMNLNotFoundError(TRMNLError):
    """The resource does not exist."""
