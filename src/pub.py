class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def count_drinks(self):
        return len(self.drinks)

    def search_for_order(self, order):
        for drink in self.drinks:
            if drink.name == order:
                return drink
        return  "Sorry, we don't have that drink!"

    def check_customer_money(self, customer):
        drink = self.search_for_order(customer.order)
        if customer.wallet >= drink.price:
            return True
        return "Can't afford"

    def serve_customer_drink(self, customer):
        if self.check_customer_money(customer):
            drink = self.search_for_order(customer.order)
            customer.wallet -= drink.price
            self.till += drink.price

