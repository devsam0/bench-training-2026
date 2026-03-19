import json
import os
import argparse
from datetime import datetime

class Task:
    def __init__(self, task_id, title, status='todo'):
        self.id = task_id
        self.title = title
        self.status = status
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        return self.__dict__

class TaskManager:
    def __init__(self):
        self.file_path = 'tasks.json'
        self.tasks = self.load_data()

    def load_data(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, 'r') as f:
                raw_data = json.load(f)
                return [Task(t['id'], t['title'], t['status']) for t in raw_data]
        except (json.JSONDecodeError, Exception) as e:
            print(f"Error loading JSON: {e}. Starting fresh.")
            return []

    def save_data(self):
        with open(self.file_path, 'w') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    def add_task(self, title):
        new_id = len(self.tasks) + 1
        self.tasks.append(Task(new_id, title))
        self.save_data()
        print(f"Success: Added task #{new_id}")

    def list_tasks(self, filter_status=None):
        print(f"\n--- {'All Tasks' if not filter_status else filter_status.upper()} ---")
        for t in self.tasks:
            if not filter_status or t.status == filter_status:
                print(f"[{t.id}] {t.title} - {t.status}")

    def complete_task(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                t.status = 'done'
                self.save_data()
                print(f"Updated: Task {task_id} is now complete.")
                return
        print(f"Error: Could not find ID {task_id}")

if __name__ == "__main__":
    manager = TaskManager()
    parser = argparse.ArgumentParser(description="My Day 3 Task Tracker")
    parser.add_argument('action', choices=['add', 'list', 'done'])
    parser.add_argument('value', nargs='?', default=None)
    parser.add_argument('--filter', help="Filter by 'todo' or 'done'")

    args = parser.parse_args()

    if args.action == 'add' and args.value:
        manager.add_task(args.value)
    elif args.action == 'list':
        manager.list_tasks(args.filter)
    elif args.action == 'done' and args.value:
        manager.complete_task(int(args.value))
    else:
        print("Usage: python tasks.py [add 'title' | list | done ID]")