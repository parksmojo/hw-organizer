from task import Task

class Organizer:
    def __init__(self) -> None:
        self.tasks: set = set()
    
    def addTask(self, course, name, due, prep=0, priority=0):
        self.tasks.add(Task(course, name, due, prep, priority))

    def __str__(self):
        output: str = ''
        for item in self.tasks:
            output += item.__str__()
            output += '\n'
        return output