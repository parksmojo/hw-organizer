class Task:
    def __init__(self, course=None, name='', due=0, prep=0, priority=0, done=False) -> None:
        self.course = course
        self.name = name
        self.due = due
        self.prep = prep
        self.priority = priority
        self.done = done

    def complete(self):
        self.done = True

    def __str__(self):
        if self.done:
            done: str = ', Completed'
        else:
            done: str = ''

        start = self.due - self.prep

        return (f"{self.course}, \"{self.name}\", Due in {self.due} days, "
                f"Start in {start} days, {self.priority} priority{done}")
