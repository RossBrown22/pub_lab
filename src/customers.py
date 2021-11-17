class Customers:
    def __init__(self, name, wallet, order):
        self.name = name
        self.wallet = wallet
        self.order = order
        self.customers = []
    
    def reduce_cash(self, amount):
        self.wallet -= amount

    def add_customer_to_list(self, customer):
        self.customers.append(customer)