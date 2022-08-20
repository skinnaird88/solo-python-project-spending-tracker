from models.transaction import Transaction
from models.tag import Tag
from models.merchant import Merchant

import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository

tag1 = Tag("groceries")
tag2 = Tag("motor")

tags = [tag1, tag2]

merchant1 = Merchant("Tesco", "groceries")
merchant2 = Merchant("Shell", "motor")

merchants = [merchant1, merchant2]

transaction1 = Transaction("Chocolate", tag1, 1, merchant1)
transaction2 = Transaction("Unleaded fuel", tag2, 50, merchant2)

transactions = [transaction1, transaction2]