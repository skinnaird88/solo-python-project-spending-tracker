from db.run_sql import run_sql
from models import merchant

from models.transaction import Transaction
# from models.tag import Tag
# from models.merchant import Merchant

# import repositories.merchant_repository as merchant_repository
# import repositories.tag_repository as tag_repository

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
        transaction = Transaction(row['name'], row['type'], row['amount'], row['merchant'], row['id'])
        list_of_transaction_instances.append(transaction)
    return list_of_transaction_instances

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)