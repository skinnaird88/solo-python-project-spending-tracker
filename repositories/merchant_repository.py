from db.run_sql import run_sql

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
        merchant = Merchant(row['name'])
        the_merchants.append(merchant)
    return the_merchants

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)