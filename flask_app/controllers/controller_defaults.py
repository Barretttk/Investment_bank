from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#==================================
#import models from models folder
#==================================

from flask_app.models.model_user import User





# ================== default routes ===============

@app.route("/")
def index():
    # if "uuid" in session:
    #     return redirect("/dashboard")
    return render_template("login_home.html")

@app.route("/Accent_Empire/dashboard")
def dashboard():
    # if "uuid" not in session:
    #     return redirect("/")


    return render_template("dashboard.html")



@app.route('/<path:path>')
def catch_all(path):
        return 'page not found'


#================MAIN / login AND Backdoorlogin default===========

# @app.route("/Accent_Empire/Login")
# def backdoorlogin():
#         # if "uuid" not in session:
#     #     return redirect("/")

#     return render_template("login.html")


# #=================  LOGIN  ===================

# @app.route("/Accent_Empire/login", methods=['POST'])
# def user_login():
# # validate
#     model_user.User.validate_login(request.form)

# #store id in session
#     existing_user = model_user.User.get_one_by_email(request.form)

# # if user existing 
#     if existing_user :
#         if not bcrypt.check_password_hash(existing_user.password, request.form["password"]):
#             flash("wrong credentials", "err_user_password_login")

#         session["first_name"] = existing_user.first_name
#         session["email"] = existing_user.email
#         session["uuid"] = existing_user.id

#         return redirect("/dashboard")
#     else:
#         return redirect("/")




