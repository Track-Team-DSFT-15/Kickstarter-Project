"""Our Tweepy web application"""
from os import getenv
from flask import Flask, render_template, request
from .models import DB, User
from .twitter import get_info_and_add


def create_app():
    """The function that will run inside __init__.py"""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)
    # endpoint == "/"

    @app.route("/")
    def root():

        return render_template("base.html",
                               project_name=project_name,
                               )

    # endpoint == "user_submitted"

    @app.route("/user_submitted", methods=["POST"])
    def user_submitted():
        username_1 = request.values["username_1"]
        username_2 = request.values["username_2"]
        # dtypes: user = <user twitter object>, user_tweets = <tweets list>
        DB_user = get_info_and_add(username_1)
        DB_user2 = get_info_and_add(username_2)
        return render_template("user.html", username_1=username_1, username_2=username_2, tweets=DB_user.embeddings)

    # endpoint == "reset"

    @app.route("/reset")
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template("reset.html")

    return app
