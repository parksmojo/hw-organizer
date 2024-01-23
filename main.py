from organizer import Organizer
from task import Task

if __name__ == "__main__":
    hwo = Organizer()

    hwo.addTask('Rel','Weekly Practice',2)
    hwo.addTask('CS240','Phase 1',14,7)
    hwo.addTask('CS202','Lab 3',3)

    print(hwo)
