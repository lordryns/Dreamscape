from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint( "auth", __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def register():
    error_message = ""
    is_error = False 

    is_success = False


    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if (len(password) >= 8):
            is_error = False
            is_success = True 
            redirect(url_for("views.home"))
        else:
            error_message = "Password must be at least 8 characters long."
            is_error = True


        print(username, email, password)
    return render_template("register.html", error_message=error_message, is_error=is_error, is_success=is_success)
