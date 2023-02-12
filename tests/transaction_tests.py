import unittest
from console import transaction1, transaction2, tag1, merchant2

class TestTransaction(unittest.TestCase):
    def test_transaction_amount(self):
        self.assertEqual(1, transaction1.amount)

    # def test_transaction_desc(self):
    #     self.assertEqual("Unleaded fuel", transaction2.description)

    # def test_transaction_tag(self):
    #     self.assertEqual(tag1, transaction1.type)
    

    def test_transaction_merchant(self):
        self.assertEqual(merchant2, transaction2.merchant)


