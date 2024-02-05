from interface import Interface
from organizer import Organizer

if __name__ == "__main__":
    hwo = Organizer()
    hwo.addTask('CS252','HW2',0)
    hwo.addTask('CS252','TA3',5,1)
    hwo.addTask('CS240','Phase1',12,7)

    Interface()
