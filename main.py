from organizer import Organizer

if __name__ == "__main__":
    hwo = Organizer()
    print(hwo)

    print(hwo.addTask('CS240','Phase1',14,7))
    print(hwo.addTask('CS230','Phase1',14,7))
    print(hwo.addTask('CS244','Phase2',10,7))
    print(hwo.addTask('CS240','Phase2',14,7))
    print(hwo)
    
    print(hwo.addTask('CS240','Phase2',14,7))
    print(hwo)

    hwo.clear()
    print(hwo)
