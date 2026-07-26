import unittest
from packages.core import Engine, Agent, Task

class TestCore(unittest.TestCase):
    def test_register_agent(self):
        engine = Engine()
        agent_id = 'agent-1'
        agent_type = 'type-1'
        engine.register_agent(agent_id, agent_type)
        self.assertIn(agent_id, engine.agents)

    def test_assign_task(self):
        engine = Engine()
        agent_id = 'agent-1'
        agent_type = 'type-1'
        task_id = 'task-1'
        task_type = 'type-1'
        engine.register_agent(agent_id, agent_type)
        task = Task(task_id, agent_id, task_type)
        engine.assign_task(agent_id, task)
        self.assertIn(task, engine.tasks)

    def test_execute_tasks(self):
        engine = Engine()
        agent_id = 'agent-1'
        agent_type = 'type-1'
        task_id = 'task-1'
        task_type = 'type-1'
        engine.register_agent(agent_id, agent_type)
        task = Task(task_id, agent_id, task_type)
        engine.assign_task(agent_id, task)
        engine.execute_tasks()
        self.assertEqual(task.status, 'pending')
