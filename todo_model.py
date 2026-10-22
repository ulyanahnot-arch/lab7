import uuid
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional

class TaskStatus(Enum):
    TODO = "ToDo"
    IN_PROGRESS = "InProgress"
    DONE = "Done"

@dataclass
class Task:
    description: str
    schedule_for: datetime
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: datetime = field(default_factory=datetime.now)
    status: TaskStatus = TaskStatus.TODO

class TaskModel:
    def __init__(self):

        self._tasks: List[Task] = []

    def add_task(self, description: str, schedule_for: datetime) -> Task:
        task = Task(description=description, schedule_for=schedule_for)
        self._tasks.append(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        return self._tasks

    def get_task_by_id(self, task_id_str: str) -> Optional[Task]:

        for task in self._tasks:
            if str(task.id).startswith(task_id_str):
                return task
        return None

    def filter_by_status(self, status: TaskStatus) -> List[Task]:
        return [task for task in self._tasks if task.status == status]

    def update_task_status(self, task_id_str: str, new_status: TaskStatus) -> bool:
        task = self.get_task_by_id(task_id_str)
        if task:
            task.status = new_status
            return True
        return False
        
    def update_task_description(self, task_id_str: str, new_desc: str) -> bool:
        task = self.get_task_by_id(task_id_str)
        if task:
            task.description = new_desc
            return True
        return False

    def delete_task(self, task_id_str: str) -> bool:
        task = self.get_task_by_id(task_id_str)
        if task:
            self._tasks.remove(task)
            return True
        return False