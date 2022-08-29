from classes.Storage import Storage
from classes.exeptions import NotPlaceForItems, NotEnoughItems, NotFoundItems


class BaseStore(Storage):
    def __init__(self):
        self._items = dict()
        self._capacity = 0

    @property
    def capacity(self):
        return self._capacity

    @property
    def items(self):
        return self._items

    def add(self, title, count):
        if count > self.get_free_space():
            raise NotPlaceForItems('Недостаточно места')
        self.items[title] = self.items.get(title, 0) + count

    def remove(self, title, count):
        if self.items.get(title) is None:
            raise NotFoundItems("Такой товар не найден")
        if count < self.get_free_space():
            self.items[title] = self.items.get(title) - count
        elif count > self.items[title] == 0:
            raise NotEnoughItems("Недостаточно товаров")

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(set(self.items.keys()))