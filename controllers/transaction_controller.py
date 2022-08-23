from crypt import methods
from flask import Flask, render_template, request, redirect
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
    return render_template("transactions/index.html", the_transactions = transactions)

# @merchants_blueprint.route("/merchants/<id>")
# def show(id):
#     merchant = merchant_repository.select(id)
#     tags = merchant_repository.tags(merchant)
#     return render_template("merchants/show.html", merchant=merchant, tags=tags)

@transactions_blueprint.route("/transactions/add", methods=['GET'])
def add_new_transaction():
    transactions = transaction_repository.select_all()
    return render_template("transactions/add.html", transactions = transactions)

@transactions_blueprint.route("/tags", methods=['POST'])
def create_new_transaction():
    name = request.form['name']
    type = request.form['type']
    amount = request.form['amount']
    merchant = request.form['merchant']
    transaction = Transaction(name, type, amount, merchant)
    transaction_repository.create(transaction)
    return redirect('/transactions')