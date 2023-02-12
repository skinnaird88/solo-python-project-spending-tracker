import unittest
from console import merchant1, merchant2

class MerchantTest(unittest.TestCase):
    def test_merchant_has_name(self):
        self.assertEqual("Tesco", merchant1.name)

    # def test_merchant_type(self):
    #     self.assertEqual("motor", merchant2.type)
