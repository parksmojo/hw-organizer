from organizer import Organizer

class Interface:
    def __init__(self) -> None:
        self.running = True
        self.hwo = Organizer()
        self.process()

    def process(self):
        while(self.running):
            usrinput = input("Command: ")

            match usrinput:
                case "quit" | "Quit" | 'q':
                    self.running = False
                case 'print' | 'Print' | 'p':
                    print(self.hwo)
                case _ :
                    print(f"Command not recognized: {usrinput}")
