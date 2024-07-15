from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint( "auth", __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def register():
    from . import account

    error_message = ""
    is_error = False 

    is_success = False


    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if (len(password) >= 8):
            try:
                result = account.create(
                    user_id = str(uuid.uuid4),
                    email = email,
                    password = password,
                    name = username # optional
                )
                is_error = False
                is_success = True 
                return redirect(url_for("views.home"))
            except Exception as e:
                is_error = True
                error_message = str(e)
        
        else:
            error_message = "Password must be at least 8 characters long."
            is_error = True


        print(username, email, password)
    return render_template("register.html", error_message=error_message, is_error=is_error, is_success=is_success)
