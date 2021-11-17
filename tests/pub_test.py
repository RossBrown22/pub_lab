import unittest
from src.pub import Pub
from src.drink import Drink
from src.customers import Customers

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink1 = Drink("Martini", 5)
        self.drink2 = Drink("Beer", 3)
        self.drink3 = Drink("Water", 10)
        self.pub.drinks = (self.drink1, self.drink2, self.drink3)
        self.customer = Customers("Walter", 1000, "Water")

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)

    def test_count_drinks(self):
        count = self.pub.count_drinks()
        self.assertEqual(3, count)
    
    def test_search_for_order(self):
        drink = self.pub.search_for_order(self.customer.order)
        self.assertEqual(self.drink3, drink)

    def test_check_customer_money(self):
        has_money = self.pub.check_customer_money(self.customer)
        self.assertEqual(True, has_money)
    
    def test_serve_customer_drink(self):
        self.pub.serve_customer_drink(self.customer)
        self.assertEqual(110, self.pub.till)


       