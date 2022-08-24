import pdb
from unicodedata import name
from models.transaction import Transaction
from models.tag import Tag
from models.merchant import Merchant

import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository

# merchant_repository.delete_all()
# transaction_repository.delete_all()
# tag_repository.delete_all()

tag1 = Tag("groceries")
tag2 = Tag("motor")

# tag_repository.create(tag1)

tags = [tag1, tag2]

merchant1 = Merchant("Tesco", "groceries")
merchant2 = Merchant("Shell", "motor")
# merchant_repository.create(merchant1)

merchants = [merchant1, merchant2]

transaction1 = Transaction("Chocolate", "groceries", 1, "Tesco")
transaction2 = Transaction("Unleaded fuel", tag2, 50, merchant2)

# transaction_repository.create(transaction1)

transactions = [transaction1, transaction2]

# pdb.set_trace()