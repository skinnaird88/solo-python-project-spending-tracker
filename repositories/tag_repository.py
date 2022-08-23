from db.run_sql import run_sql

from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction

def create(tag):
    sql = "INSERT INTO tags( category ) VALUES ( %s ) RETURNING id"
    values = [tag.category]
    results = run_sql( sql, values )
    tag.id = results[0]['id']
    return tag

def select_all():
    the_tags = []
    sql = "SELECT * from tags"
    rows = run_sql(sql)
    for row in rows:
        tag = Tag(row['category'])
        the_tags.append(tag)
    return the_tags



def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)
