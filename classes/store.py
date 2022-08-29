from classes.BaseStore import BaseStore


class Store(BaseStore):
    def __init__(self):
        super().__init__()
        self._capacity = 100

