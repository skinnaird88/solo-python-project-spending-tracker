from db.run_sql import run_sql
from models import merchant

from models.transaction import Transaction
# from models.tag import Tag
# from models.merchant import Merchant

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

def create(transaction):
    # transactions = []

    sql = """
    INSERT INTO transactions ( name, tag_id, amount, merchant_id ) VALUES ( %s, %s, %s, %s ) returning id"""
    values = [transaction.name, transaction.tag.id, transaction.amount, transaction.merchant.id]
    print("THIS IS VALUUUUUUUUUUUUEEEESSS", values)
    results = run_sql(sql, values)
    print("HHHHHHHHHHHHHHEEEEEEERRRRRRRREEEEEEEE IT IS", results)
    id = results[0]['id']
    transaction.id = id
    # id = results[0]['id']
    # transaction.id = id

def select_all():
    list_of_transaction_instances = []
    sql = "SELECT * from transactions"
    rows_of_transactions = run_sql(sql)

    for row in rows_of_transactions:
        # row = {'name': 'Chocolate', 'tag_id': 1...}, 
        tag = tag_repository.select(row['tag_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(row['name'], tag, row['amount'], merchant, row['id'])
        list_of_transaction_instances.append(transaction)
    return list_of_transaction_instances

def get_transaction_totals():
    total = 0
    sql = "SELECT sum(amount) as total from transactions"
    results = run_sql(sql)
    if results is not None and results[0][0] is not None:
        total = results[0]['total']
    return total

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)