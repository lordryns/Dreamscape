from flask import Blueprint, render_template, redirect, url_for

views = Blueprint( "views", __name__)

@views.route('/')
def home():
    return render_template("index.html")


@views.route('/feed')
def feed():
    from . import account

    try:
        user = account.get()
        print(user)
    except Exception as e:
        print(e)  
    return render_template("feed.html")