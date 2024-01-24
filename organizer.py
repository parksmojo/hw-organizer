from task import Task

class Organizer:
    def __init__(self) -> None:
        self.all_tasks: set[Task] = set()
        self.course_list: set[str] = set()
    
    def addTask(self, course, name, due, prep=0, priority=0):
        self.all_tasks.add(Task(course, name, due, prep, priority))

    def complete_task(self, name):
        for item in self.all_tasks:
            if item.name == name:
                item.complete()

    def __str__(self):
        output: str = 'Tasks:\n'
        for item in self.all_tasks:
            output += item.__str__()
            output += '\n'
        return output