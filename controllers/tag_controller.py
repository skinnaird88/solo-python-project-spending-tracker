from crypt import methods
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

@tags_blueprint.route("/tags/add", methods=['POST'])
def add_new_tag(tag):
    
    tag_name = request.form['tag_name']
    tag = Tag(tag_name)
    tag_repository.create(tag)
    return redirect("/tags")