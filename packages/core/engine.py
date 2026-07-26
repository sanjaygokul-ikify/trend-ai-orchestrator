import logging
from typing import List, Dict
from .types import Agent, Task
from .exceptions import EngineError, InvalidAgentError

logger = logging.getLogger(__name__)

class Engine:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.tasks: List[Task] = []

    def register_agent(self, agent_id: str, agent_type: str) -> None:
        if agent_id in self.agents:
            raise InvalidAgentError(f'Agent {agent_id} already registered')
        self.agents[agent_id] = Agent(agent_id, agent_type)
        logger.info(f'Registered agent {agent_id} of type {agent_type}')

    def assign_task(self, agent_id: str, task: Task) -> None:
        if agent_id not in self.agents:
            raise InvalidAgentError(f'Agent {agent_id} not registered')
        self.tasks.append(task)
        logger.info(f'Assigned task {task.task_id} to agent {agent_id}')

    def execute_tasks(self) -> None:
        for task in self.tasks:
            try:
                agent = self.agents[task.agent_id]
                agent.execute_task(task)
                logger.info(f'Task {task.task_id} executed successfully by agent {agent.agent_id}')
            except Exception as e:
                logger.error(f'Error executing task {task.task_id}: {str(e)}')
                raise EngineError(f'Error executing task {task.task_id}: {str(e)}')

    def get_agent_status(self, agent_id: str) -> str:
        if agent_id not in self.agents:
            raise InvalidAgentError(f'Agent {agent_id} not registered')
        return self.agents[agent_id].status

    def get_task_status(self, task_id: str) -> str:
        for task in self.tasks:
            if task.task_id == task_id:
                return task.status
        raise EngineError(f'Task {task_id} not found')

    def update_agent_status(self, agent_id: str, status: str) -> None:
        if agent_id not in self.agents:
            raise InvalidAgentError(f'Agent {agent_id} not registered')
        self.agents[agent_id].status = status
        logger.info(f'Updated agent {agent_id} status to {status}')

    def update_task_status(self, task_id: str, status: str) -> None:
        for task in self.tasks:
            if task.task_id == task_id:
                task.status = status
                logger.info(f'Updated task {task_id} status to {status}')
                return
        raise EngineError(f'Task {task_id} not found')

    def remove_agent(self, agent_id: str) -> None:
        if agent_id not in self.agents:
            raise InvalidAgentError(f'Agent {agent_id} not registered')
        del self.agents[agent_id]
        logger.info(f'Removed agent {agent_id}')

    def remove_task(self, task_id: str) -> None:
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        logger.info(f'Removed task {task_id}')
