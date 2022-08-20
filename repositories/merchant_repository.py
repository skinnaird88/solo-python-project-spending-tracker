from db.run_sql import run_sql

from models.merchant import Merchant
from models.tag import Tag

# def create(merchant):
#     sql = """
#     INSERT INTO merchants ( name, type ) VALUES ( %s, %s ) returning id
#     """
#     values = [merchant.name]
#     results = run_sql(sql, values)
#     merchant.id = results[0]['id']
#     return merchant

# def delete_all():
#     sql = "DELETE FROM merchants"
#     run_sql(sql)