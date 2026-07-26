import logging

_LOGGER = logging.getLogger(__name__)

def log_error(message: str) -> None:
    _LOGGER.error(message)

