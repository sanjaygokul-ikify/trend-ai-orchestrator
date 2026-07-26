import unittest
from services.orchestrator import Orchestrator

class TestRuntime(unittest.TestCase):
    def test_register_agent(self):
        orchestrator = Orchestrator()
        agent_id = 'agent-1'
        agent_type = 'type-1'
        orchestrator.register_agent(agent_id, agent_type)

    def test_assign_task(self):
        orchestrator = Orchestrator()
        agent_id = 'agent-1'
        agent_type = 'type-1'
        task_id = 'task-1'
        task_type = 'type-1'
        orchestrator.register_agent(agent_id, agent_type)
        orchestrator.assign_task(agent_id, task_id, task_type)

    def test_execute_tasks(self):
        orchestrator = Orchestrator()
        agent_id = 'agent-1'
        agent_type = 'type-1'
        task_id = 'task-1'
        task_type = 'type-1'
        orchestrator.register_agent(agent_id, agent_type)
        orchestrator.assign_task(agent_id, task_id, task_type)
        orchestrator.execute_tasks()
