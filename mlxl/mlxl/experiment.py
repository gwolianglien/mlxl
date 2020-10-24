

class Experiment():

    def __init__(self, task: 'object' = None, values: object = None) -> None:
        self.task = task
        self.values = values

    def get_task(self) -> object:
        return self.task

    def set_task(self, task) -> None:
        self.task = task

    def get_values(self) -> object:
        return self.values

    def set_values(self, values) -> None:
        self.values = values
