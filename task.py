class Task:
    def __init__(self, course=None, name='', due=0, prep=0, priority=0, done=False) -> None:
        self.course = course
        self.name = name
        self.due = due
        self.prep = prep
        self.done = done

        self.priorities_list: list[str] = [None,'Low','Medium','High']
        if priority < 0:
            self.priority = 0
        elif priority > 2:
            self.priority = 2
        else:
            self.priority = priority

    def complete(self):
        self.done = True

    def __str__(self):
        output = ''
        output += f'{self.course}'
        output += f', \"{self.name}\"'
        if self.due == 0:
            output += ', Due today'
        else:
            output += f', Due in {self.due} days'

        if self.prep != 0:
            output += f', Start in {self.due - self.prep} days'
        
        if self.priority != 0:
            output += f', {self.priorities_list[self.priority]} priority'
        
        if self.done:
            output += ', Completed'
        
        return output
    
    def __eq__(self, __value: object) -> bool:
        # Assuming only Task objects will be passed in
        # might need to be changed
        if (self.name == __value.name) and (self.course == __value.course) and (self.due == __value.due):
            return True
        else:
            return False
        
    def __hash__(self) -> int:
        return super.__hash__(self)
