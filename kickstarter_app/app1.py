"""Our Tweepy web application"""
from os import getenv
from flask import Flask, render_template, request
from .models import DB, User
# from .twitter import get_info_and_add
from datetime import datetime
import pandas as pd
from .prediction import predict_user

def create_app():
    """The function that will run inside __init__.py"""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)
    # endpoint == "/"

    @app.route("/")
    def root():
        return render_template("base.html")

    # Repl
    @app.route("/repl")
    def repl():
        pred = predict_user()
        return str(pred)

    # endpoint == "user_submitted"

    @app.route("/user_submitted", methods=["POST"])
    def user_submitted():
        if User.query.filter_by(id='0').count() > 0:
            id = User.query.all()[-1].id + 1
        else:
            id = 0
        project_name = request.values['project_name']
        category = request.values['category']
        main_category = request.values['main_category']
        currency = request.values['currency']
        deadline = pd.to_datetime(request.values['deadline'])
        goal = request.values['goal']
        launched = pd.to_datetime(request.values['launched'])
        pledged = request.values['pledged']
        backers = request.values['backers']
        country = request.values['country']
        usd_pledged = request.values['usd_pledged']
        usd_pledged_real = request.values['usd_pledged_real']
        usd_goal_real = request.values['usd_goal_real']
        days = deadline - launched
        days = int(days.days)

        record = User(id=id,
                      project_name=project_name,
                      category=category,
                      main_category=main_category,
                      currency=currency,
                      goal=goal,
                      pledged=pledged,
                      backers=backers,
                      country=country,
                      usd_pledged=usd_pledged,
                      usd_pledged_real=usd_pledged_real,
                      usd_goal_real=usd_goal_real,
                      days=days)
        DB.session.add(record)
        DB.session.commit()
        return render_template("user.html",
                               project_name=project_name,
                               category=category,
                               main_category=main_category,
                               currency=currency,
                               deadline=deadline,
                               goal=goal,
                               launched=launched,
                               pledged=pledged,
                               backers=backers,
                               country=country,
                               usd_pledged=usd_pledged,
                               usd_pledged_real=usd_pledged_real,
                               usd_goal_real=usd_goal_real)

    # endpoint == "reset"

    @app.route("/reset")
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template("reset.html")

    return app


