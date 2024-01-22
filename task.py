class Task:
    def __init__(self, course, name, due, prep, priority, done=False) -> None:
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
            done: str = 'Completed'
        else:
            done: str = 'Not Completed'

        start = self.due - self.prep

        return (f"{self.course}, \"{self.name}\", Due by:{self.due}, "
                f"Start by:{start}, {self.priority} priority, {done}")
