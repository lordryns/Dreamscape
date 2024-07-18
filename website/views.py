from flask import Blueprint, render_template, redirect, url_for

views = Blueprint( "views", __name__)

@views.route('/')
def home():
    return render_template("index.html")


@views.route('/feed')
def feed():
    from . import account

    error_message: str = ""
    is_error: bool = False
    is_success: bool = False
    try:
        user = account.get()
        print(user)
        is_success = True
        
    except Exception as e:
        is_error = True 
        error_message = str(e)
        
    return render_template("feed.html", is_error=is_error, error_message=error_message, is_success=is_success)