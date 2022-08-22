from flask import Flask, render_template
from flask import Blueprint

# import repositories.transaction_repository as transaction_repository
# import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all() 
    return render_template("tags/index.html")

@tags_blueprint.route("/tags/add")
def add_new_tag():
    new_tag = tag_repository.create
    return render_template("tags/add.html")