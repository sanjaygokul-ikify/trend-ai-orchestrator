from typing import Type, Any

class TrendOrchestratorError(Exception):
    pass

class InvalidSyntaxError(TrendOrchestratorError):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f'Invalid syntax: {self.message}'

class Agent:
    def __init__(self, agent_id: str, agent_type: str):
        self.agent_id = agent_id
        self.agent_type = agent_type
        self.status = 'registered'

    def execute_task(self, task: 'Task') -> None:
        # task execution logic here
        self.status = 'executing'

    def __str__(self) -> str:
        return f'Agent({self.agent_id}, {self.agent_type})'

class Task:
    def __init__(self, task_id: str, agent_id: str, task_type: str):
        self.task_id = task_id
        self.agent_id = agent_id
        self.task_type = task_type
        self.status = 'pending'

    def __str__(self) -> str:
        return f'Task({self.task_id}, {self.agent_id}, {self.task_type})'
