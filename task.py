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
        output += f', \"{self.name}\"\n'
        for i in range(len(f'{self.course}, ')):
            output += ' '
        output += f'-Due in {self.due} days'

        if self.prep != 0:
            output += f', Start in {self.due - self.prep} days'
        
        if self.priority != 0:
            output += f', {self.priorities_list[self.priority]} priority'
        
        if self.done:
            output += ', Completed'
        
        # output += '\n'
        return output
