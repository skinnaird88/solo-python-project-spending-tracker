from db.run_sql import run_sql

from models.transaction import Transaction
from models.tag import Tag
from models.merchant import Merchant

import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository

def create(transaction):
    # transactions = []

    sql = """
    INSERT INTO transactions ( name ) VALUES ( %s, %s, %s, %s ) returning *"""
    values = [transaction.description]
    # removed transaction.type, transaction.amount, transaction.merchant] ^^^^
    results = run_sql(sql, values)
    transaction.id = results
    return transaction

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)