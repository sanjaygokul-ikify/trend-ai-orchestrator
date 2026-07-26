import argparse
from services.orchestrator import Orchestrator

parser = argparse.ArgumentParser(description='AI Orchestrator CLI')
subparsers = parser.add_subparsers(dest='command')

register_parser = subparsers.add_parser('register', help='Register an agent')
register_parser.add_argument('--agent-id', required=True)
register_parser.add_argument('--agent-type', required=True)

assign_parser = subparsers.add_parser('assign', help='Assign a task to an agent')
assign_parser.add_argument('--agent-id', required=True)
assign_parser.add_argument('--task-id', required=True)
assign_parser.add_argument('--task-type', required=True)

execute_parser = subparsers.add_parser('execute', help='Execute tasks')

args = parser.parse_args()

orchestrator = Orchestrator()

if args.command == 'register':
    orchestrator.register_agent(args.agent_id, args.agent_type)
elif args.command == 'assign':
    orchestrator.assign_task(args.agent_id, args.task_id, args.task_type)
elif args.command == 'execute':
    orchestrator.execute_tasks()
