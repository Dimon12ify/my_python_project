from Order import Order


class Cart:
    def __init__(self, user):
        self.user = user
        self.orders = list()

    def add_item(self, order: Order):
        message = ""
        is_added = False
        if order is None:
            message = "Пустой заказ"
        if order.name == "":
            message = "Пустое имя товара"
        if order.quantity < 1:
            message = "Неверное количество товара"
        if order.price < 0:
            message = "Неверная цена товара"
        if not is_added:
            print(message)
            return False
        self.orders.append(order)
        return True

    def remove_item(self):
        pass

    def current_cost(self):
        pass

    def buy_orders(self):
        pass

