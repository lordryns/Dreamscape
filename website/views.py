from flask import Blueprint, render_template, redirect, url_for

views = Blueprint( "views", __name__)

@views.route('/')
def home():
    return render_template("index.html")


@views.route('/feed')
def feed():
    from . import account
   
    return render_template("feed.html")