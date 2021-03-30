"""Our Tweepy web application"""
from os import getenv
from flask import Flask, render_template, request
from .models import DB, User
# from .twitter import get_info_and_add
from datetime import datetime

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

    # endpoint == "user_submitted"

    @app.route("/user_submitted", methods=["POST"])
    def user_submitted():
        project_name = request.values['project_name']
        category = request.values['category']
        main_category = request.values['main_category']
        currency = request.values['currency']
        deadline = datetime.strptime(request.values['deadline'], '%Y-%m-%d')
        goal = request.values['goal']
        launched = datetime.strptime(request.values['launched'], '%Y-%m-%d')
        pledged = request.values['pledged']
        backers = request.values['backers']
        country = request.values['country']
        usd_pledged = request.values['usd_pledged']
        usd_pledged_real = request.values['usd_pledged_real']
        usd_goal_real = request.values['usd_goal_real']
        # username_1 = request.values["username_1"]
        # username_2 = request.values["username_2"]
        # dtypes: user = <user twitter object>, user_tweets = <tweets list>
        # DB_user = get_info_and_add(username_1)
        # DB_user2 = get_info_and_add(username_2)
        record = User(project_name=project_name,
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
