import unittest
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from console import *

from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def my_merchants():
    merchants = merchant_repository.select_all()
    print ("HHHEEEEEEYYYYYYY", merchants)
    return render_template("merchants/index.html", the_merchants = merchants)

# @merchants_blueprint.route("/merchants/<id>")
# def show(id):
#     merchant = merchant_repository.select(id)
#     tags = merchant_repository.tags(merchant)
#     return render_template("merchants/show.html", merchant=merchant, tags=tags)

# @merchants_blueprint.route("/merchants/add")
# def add_new_merchant():
#     new_merchant = merchant_repository.create
#     return render_template("merchants/add.html")

@merchants_blueprint.route("/merchants/add", methods=['GET'])
def add_new_merchant():
    merchants = merchant_repository.select_all()
    return render_template("merchants/add.html", merchants = merchants)

@merchants_blueprint.route("/merchants", methods=['POST'])
def create_new_merchant():
    name = request.form['name']
    merchant = Merchant(name)
    merchant_repository.create(merchant)
    return redirect('/merchants')

@merchants_blueprint.route("/merchants/<id>/edit", methods=['GET'])
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/edit.html', merchant = merchant)

@merchants_blueprint.route("/merchants/<id>", methods=['POST'])
def update_merchant(id):
    name = request.form['name']
    updated_merchant = Merchant(name, id)
    merchant_repository.update_merchant(updated_merchant)
    return redirect('/merchants')