from typing import Type, Any

class TrendOrchestratorError(Exception):
    pass

class InvalidSyntaxError(TrendOrchestratorError):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f'Invalid syntax: {self.message}'

