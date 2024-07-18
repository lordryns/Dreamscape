from flask import Blueprint, render_template, request, redirect, url_for, session
import base64
import uuid

auth = Blueprint( "auth", __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def register():

    if "id" not in session:
        session["username"] = None 
        session["email"] = None
        session["id"] = None 
        session["labels"] = None

    from . import account, users

    error_message = ""
    is_error = False 

    is_success = False


    if request.method == 'POST':

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        my_uuid = uuid.uuid4()
        base64_uuid = base64.urlsafe_b64encode(my_uuid.bytes).decode('utf-8').rstrip('=')

        if (len(password) >= 8):
            try:
                result = account.create(
                    user_id = "unique()",
                    email = email,
                    password = password,
                    name = username # optional
                )

                
                session_token = account.create_email_password_session(email, password)
                user = users.get(
                    user_id = session_token['userId']
                )

                session["username"] = user['name']
                session["email"] = user['email']
                session["id"] = session_token['userId']
                session["labels"] = user['labels']

                print(user)
                
                is_error = False
                is_success = True 
                
                return redirect(url_for("views.feed"))
            except Exception as e:
                is_error = True
                error_message = str(e)
        
        else:
            error_message = "Password must be at least 8 characters long."
            is_error = True


    return render_template("register.html", error_message=error_message, is_error=is_error, is_success=is_success)
