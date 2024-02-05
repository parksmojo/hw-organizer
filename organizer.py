import pickle, os
from task import Task

class Organizer:
    def __init__(self) -> None:
        self.all_tasks: list[Task] = []
        with open('task_data.txt', 'rb') as f:
            f.seek(0, os.SEEK_END) # go to end of file
            if f.tell(): # if current position is truish (i.e != 0)
                f.seek(0) # rewind the file for later use 
                self.all_tasks = pickle.load(f)

        self.course_list: set[str] = set()
    
    def addTask(self, course, name, due, prep=0, priority=0) -> bool:
        exists: bool = False
        temp: Task = Task(course, name, due, prep, priority)

        for item in self.all_tasks:
            if item == temp:
                exists = True
                break
            
        if exists:
            del temp
            return False
        else:
            self.all_tasks.append(temp)
            self.save()
            return True

    def complete_task(self, name):
        for item in self.all_tasks:
            if item.name == name:
                item.complete()
        self.save()

    def save(self):
        with open('task_data.txt', 'wb') as f:
            pickle.dump(self.all_tasks, f)
    
    def clear(self):
        self.all_tasks.clear()
        self.save()

    def __str__(self):
        output: str = 'Tasks:\n'
        if len(self.all_tasks) == 0:
            output += 'No tasks'
        else:        
            for i in range(len(self.all_tasks)):
                output += f"[{i}] "
                output += self.all_tasks[i].__str__()
                output += '\n'
        return output