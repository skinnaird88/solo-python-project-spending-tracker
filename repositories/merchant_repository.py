from db.run_sql import run_sql
from models import merchant

from models.merchant import Merchant

def create(merchant):
    sql = """
    INSERT INTO merchants ( name ) VALUES ( %s ) returning id
    """
    values = [merchant.name]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']
    return merchant

def select_all():
    the_merchants = []
    sql = "SELECT * from merchants"
    rows = run_sql(sql)
    for row in rows:
        merchant = Merchant(row['name'], row['id'])
        the_merchants.append(merchant)
    return the_merchants

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['id'])
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def update_merchant(merchant):
    sql = "UPDATE merchants SET name = %s WHERE id = %s"
    values = [merchant.name, merchant.id]
    run_sql(sql, values)