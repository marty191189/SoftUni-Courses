from project.worker import Worker


class Keeper(Worker):

    def __init__(self, name, age, salary):
        Worker.__init__(self, name, age, salary)
