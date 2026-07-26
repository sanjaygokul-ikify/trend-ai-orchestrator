from packages.core import Engine
from packages.utils import get_logger

logger = get_logger(__name__)

class Orchestrator:
    def __init__(self):
        self.engine = Engine()

    def register_agent(self, agent_id: str, agent_type: str) -> None:
        try:
            self.engine.register_agent(agent_id, agent_type)
        except Exception as e:
            logger.error(f'Error registering agent {agent_id}: {str(e)}')

    def assign_task(self, agent_id: str, task_id: str, task_type: str) -> None:
        try:
            task = Task(task_id, agent_id, task_type)
            self.engine.assign_task(agent_id, task)
        except Exception as e:
            logger.error(f'Error assigning task {task_id} to agent {agent_id}: {str(e)}')

    def execute_tasks(self) -> None:
        try:
            self.engine.execute_tasks()
        except Exception as e:
            logger.error(f'Error executing tasks: {str(e)}')
