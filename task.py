class Task:
    def __init__(self, course: str, name: str, due, prep: int, priority, done: bool) -> None:
        self.course = course
        self.name = name
        self.due = due
        self.prep = prep
        self.priority = priority
        self.done = done

    def __str__(self):
        if self.done:
            finished = 'Completed'
        else:
            finished = 'Not Completed'

        start = self.due - self.prep

        return (f"{self.course}, \"{self.name}\", Due by:{self.due}, "
                f"Start by:{start}, {self.priority} priority, {finished}")
