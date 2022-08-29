from classes.exeptions import RequestTextError, NotEnoughItems, NotFoundItems, NotPlaceUniqueItems, NotPlaceForItems
from classes.request import Request
from classes.Shop import Shop
from classes.store import Store
from const\
import START_TEXT, ACTIONS_TEXT

input(START_TEXT)
store = Store()
store.add("печеньки", 1)
store.add("конфеты", 10)
store.add("шоколад", 15)
store.add("мармелад", 5)
store.add("сгущенка", 15)
store.add("пепси", 15)

shop = Shop()
shop.add("конфеты", 1)
shop.add("пепси", 2)
shop.add("шоколад", 3)
shop.add("мармелад", 2)
shop.add("сгущенка", 4)

while True:

    user_input = input('>>>').lower().strip()

    if user_input in ('exit', 'выход'):
        print('До новых встреч')
        quit()

    try:
        request = Request(user_input)
    except RequestTextError as e:
        print(e)
        continue

    try:
        if request.from_ == 'склад':
            store.remove(request.product, request.amount)
            shop.add(request.product, request.amount)
        if request.from_ == 'магазин':
            shop.remove(request.product, request.amount)
            store.add(request.product, request.amount)
    except (NotEnoughItems,
            NotFoundItems,
            NotPlaceUniqueItems,
            NotPlaceForItems) as e:
        print(e)
        continue

    print(
        ACTIONS_TEXT.format(
            amount=request.amount,
            product=request.product,
            from_=request.from_,
            to=request.to
        )
    )