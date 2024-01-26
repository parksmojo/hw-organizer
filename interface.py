from organizer import Organizer

class Interface:
    def __init__(self) -> None:
        self.running = True
        self.hwo = Organizer()
        self.process()

    def process(self):
        while(self.running):
            usrinput = input('Command: ')

            match usrinput:
                case 'q' | 'quit' | 'Quit':
                    self.running = False
                case 'p' | 'print' | 'Print':
                    print(self.hwo)
                case 'a' | 'add':
                    self.addTask()
                case 'cleartasks':
                    self.hwo.clear()
                case _ :
                    print(f'Command not recognized: {usrinput}')

    def addTask(self):
        course = input('Input course name: ')
        name = input('Input task name: ')
        due = input('In how many days is the due date? ')
        if self.hwo.addTask(course,name,int(due)):
            print('Task added successfully')
        else:
            print('Task already in organizer')
        
