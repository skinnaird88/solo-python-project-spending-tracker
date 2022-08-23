from crypt import methods
from unicodedata import category
from db.run_sql import run_sql
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag

# import repositories.transaction_repository as transaction_repository
# import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all() 
    print(tags)
    return render_template("tags/index.html", the_tags = tags)

# def other_add_new_tag (["GET"]) route:tags/add

@tags_blueprint.route("/tags/add", methods=['GET'])
def add_new_tag():
    tags = tag_repository.select_all()
    return render_template("tags/add.html", tags = tags)

@tags_blueprint.route("/tags", methods=['POST'])
def create_new_tag():
    category = request.form['category']
    tag = Tag(category)
    tag_repository.create(tag)
    return redirect('/tags')

    # new_tag = Tag(tag)
    # tag = tag_repository.select_all() 
    # tag_repository.create(new_tag)
    # return redirect("/tags")
    # tag_name = request.form['tag_name']
    # tag = Tag(tag_name)
    # tag_repository.create(tag)
    # return redirect("/tags")