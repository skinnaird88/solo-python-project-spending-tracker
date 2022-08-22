from db.run_sql import run_sql

from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction

def create(tag):
    sql = "INSERT INTO tags( name ) VALUES ( %s ) RETURNING id"
    values = [tag.name]
    results = run_sql( sql, values )
    tag.id = results[0]['id']
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)
