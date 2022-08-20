import unittest
from console import transaction1, transaction2

class TestTransaction(unittest.TestCase):
    def test_transaction_amount(self):
        self.assertEqual(1, transaction1.amount)

    def check_transaction_tag(self):
        self.assertEqual("Unleaded fuel", transaction2.description)


