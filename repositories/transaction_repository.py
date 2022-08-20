from db.run_sql import run_sql

from models.transaction import Transaction
from models.tag import Tag
from models.merchant import Merchant

import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository

def create(transaction):
    sql = """
    INSERT INTO transactions ( name, type, amount, merchant ) VALUES ( %s, %s, %s, %s ) returning id"""
    values = [transaction.description, transaction.type, transaction.amount, transaction.merchant]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction