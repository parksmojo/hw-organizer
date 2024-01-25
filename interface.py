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
                case 'cleartasks':
                    self.hwo.clear()
                case _ :
                    print(f'Command not recognized: {usrinput}')
