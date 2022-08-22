from flask import Flask, render_template
from flask import Blueprint

from models.transaction import Transaction
from models.merchant import Merchant
# from models.tag import Tag

import repositories.transaction_repository as transaction_repository
# import repositories.merchant_repository as merchant_repository
# import repositories.tag_repository as tag_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions = transactions)

# @merchants_blueprint.route("/merchants/<id>")
# def show(id):
#     merchant = merchant_repository.select(id)
#     tags = merchant_repository.tags(merchant)
#     return render_template("merchants/show.html", merchant=merchant, tags=tags)

@transactions_blueprint.route("/transactions/add")
def add_new_transaction():
    new_transaction = transaction_repository.create
    return render_template("transactions/add.html")