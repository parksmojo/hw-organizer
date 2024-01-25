from organizer import Organizer

class Interface:
    def __init__(self) -> None:
        self.running = True
        self.process()

    def process(self):
        while(self.running):
            usrinput = input("Command: ")

            if usrinput == "quit":
                self.running = False
            else:
                print(usrinput)
