from db.run_sql import run_sql

from models.transaction import Transaction
# from models.tag import Tag
# from models.merchant import Merchant

# import repositories.merchant_repository as merchant_repository
# import repositories.tag_repository as tag_repository

def create(transaction):
    # transactions = []

    sql = """
    INSERT INTO transactions ( name, type, amount, merchant ) VALUES ( %s, %s, %s, %s ) returning *"""
    values = [transaction.name, transaction.type, transaction.amount, transaction.merchant]
    # removed transaction.type, transaction.amount, transaction.merchant] ^^^^
    results = run_sql(sql, values)
    transaction.id = results
    return

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