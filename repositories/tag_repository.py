from db.run_sql import run_sql

from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)
