from classes.exeptions import RequestTextError


class Request:

    def __init__(self, req: str):
        self.req = req.split()

        try:

            shop_idx = self.req.index('магазин')
            store_idx = self.req.index('склад')
            if store_idx < shop_idx:
                self.from_ = self.req[store_idx]
                self.to = self.req[shop_idx]

            if store_idx > shop_idx:
                self.from_ = self.req[shop_idx]
                self.to = self.req[store_idx]

            self.product = self.req[self.req.index('из') - 1]

            amount = self.req[self.req.index(self.product) - 1]
            if not amount.isdigit():
                self.amount = None
            self.amount = int(amount)

        except (ValueError, IndexError):
            raise RequestTextError("Неверный формат строки"
                                   "\nПример: 'Доставить 3 печеньки из склад в магазин'")