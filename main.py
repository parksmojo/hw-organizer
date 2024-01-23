from organizer import Organizer
from task import Task

if __name__ == "__main__":
    tasks = [Task('Rel','Weekly Practice',2),
             Task('CS240','Phase 1',14,7),
             Task('CS202','Lab 3',3)]
    for item in tasks:
        print(item)
    pass
