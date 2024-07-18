from flask import Blueprint, render_template, redirect, url_for, session

views = Blueprint( "views", __name__)

@views.route('/')
def home():
    return render_template("index.html")


@views.route('/feed')
def feed():
    if "id" not in session:
        session["username"] = None 
        session["email"] = None
        session["id"] = None 
        session["labels"] = None

    from . import account

    error_message: str = ""
    is_error: bool = False
    is_success: bool = False
    
    
    if session["id"] is None:
        return redirect(url_for("auth.register"))
    
    return render_template("feed.html", is_error=is_error, error_message=error_message, is_success=is_success)