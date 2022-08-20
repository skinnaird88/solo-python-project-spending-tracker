import unittest
from flask import Flask
from flask import Blueprint
from console import *

from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

class MerchantTest(unittest.TestCase):
    def test_tag1(self):
        self.assertEqual("groceries", tag_repository.tag1)