from typing import List
from ..core.engine import Engine
from ..core.types import Task
import logging
import time

logger = logging.getLogger(__name__)

class Executor:
    def __init__(self, engine: Engine, timeout: int = 60):
        self.engine = engine
        self.timeout = timeout

    def execute(self, tasks: List[Task]) -> None:
        for task in tasks:
            try:
                start_time = time.time()
                self.engine.assign_task(task.agent_id, task)
                self.engine.execute_tasks()
                end_time = time.time()
                elapsed_time = end_time - start_time
                if elapsed_time > self.timeout:
                    logger.error(f'Task {task.task_id} timed out after {elapsed_time} seconds')
                else:
                    logger.info(f'Task {task.task_id} executed successfully in {elapsed_time} seconds')
            except Exception as e:
                logger.error(f'Error executing task {task.task_id}: {str(e)}')

    def get_status(self) -> str:
        return 'running'

    def start(self) -> None:
        logger.info('Executor started')

    def stop(self) -> None:
        logger.info('Executor stopped')