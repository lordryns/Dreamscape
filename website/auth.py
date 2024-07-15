from flask import Blueprint, render_template, request

auth = Blueprint( "auth", __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")



        print(username, email, password)
    return render_template("register.html")
