class CashRegister:

    def __init__(self, items):

  self.items = {item: False for item in items}
        self.total_items = {}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item_and_price):
        self.total_items.update(item_and_price)

    def remove_item(self, item):
        self.total_items.pop(item)

    def apply_discount(self, monetary_amount):
        Self.discount += monetary_amount

    def get_total(self, item):
        Total_before_discount = sum(self.total_items.values())
  Total = total_before_discount - self.discount

    def show_items(self):
For item, price in self.total_items.items():
Print (f”{total} £{price}”)

    def reset_register(self, item):
        self.total_items = {}
        self.total_price = 0
        self.discount = 0



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

