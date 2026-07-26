from typing import List
from ..core.engine import Engine
from ..core.types import Task
import logging

logger = logging.getLogger(__name__)

class Executor:
    def __init__(self, engine: Engine):
        self.engine = engine

    def execute(self, tasks: List[Task]) -> None:
        for task in tasks:
            self.engine.assign_task(task.agent_id, task)
            self.engine.execute_tasks()
            logger.info(f'Task {task.task_id} executed successfully')

    def get_status(self) -> str:
        return 'running'

    def start(self) -> None:
        logger.info('Executor started')

    def stop(self) -> None:
        logger.info('Executor stopped')