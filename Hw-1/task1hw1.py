class CashRegister:

    def __init__(self):

        self.total_items = {}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item_and_price):
        self.total_items.update(item_and_price)

    def remove_item(self, item):
        self.total_items.pop(item)

    def apply_discount(self, monetary_amount):
        self.discount += monetary_amount

    def get_total(self):
        total_before_discount = sum(self.total_items.values())
        total = total_before_discount - self.discount
        return total

    def show_items(self):
        for item, price in self.total_items.items():
            print(f"{item} £{price}")

    def reset_register(self):
        self.total_items = {}
        self.total_price = 0
        self.discount = 0


register_1 = CashRegister()

#Add
register_1.add_item({"Coffee": 2.00})
register_1.add_item({"Hummus": 1.50})
register_1.add_item({"Milk": 0.90})

#Remove
register_1.remove_item("Hummus")

#Discount
register_1.apply_discount(0.50)

#Total price
print(register_1.get_total())

#Customer wants receipt
register_1.show_items()

#New customer
register_1.reset_register()

