from flask import Blueprint, render_template

auth = Blueprint( "auth", __name__)

@auth.route('/signup', methods=['POST'])
def register():
    
    return render_template("register.html")
