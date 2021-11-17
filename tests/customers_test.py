import unittest
from src.customers import *

class TestCustomer (unittest.TestCase):
    def setUp(self):
        self.customer = Customers("Gilburt", 100, "Beer")
    
    def test_customer_name(self):
        self.assertEqual("Gilburt", self.customer.name)

    def test_reduce_cash(self):
        self.customer.reduce_cash(10)
        self.assertEqual(90, self.customer.wallet)

    def test_add_customer_to_list(self):
        self.customer.add_customer_to_list(self.customer)
        self.assertEqual(1, len(self.customer.customers))
    
   
