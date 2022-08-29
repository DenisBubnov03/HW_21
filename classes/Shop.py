from classes.BaseStore import BaseStore
from classes.exeptions import NotPlaceUniqueItems


class Shop(BaseStore):
    def __init__(self):
        super().__init__()
        self._capacity = 20

    def add(self, title, count):
        if title not in self.items.keys():
            if self.get_unique_items_count() == 5:
                raise NotPlaceUniqueItems("Нет свободного места для еще одного уникального товара")
            super().add(title, count)
