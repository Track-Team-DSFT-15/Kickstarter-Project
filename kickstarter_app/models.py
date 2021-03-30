from flask_sqlalchemy import SQLAlchemy

# Creating DB
DB = SQLAlchemy()


# Creating a user table
class User(DB.Model):
    """Stores values input by the user"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    project_name = DB.Column(DB.String(100), nullable=False)
    category = DB.Column(DB.String(50), nullable=False)
    main_category = DB.Column(DB.String(50), nullable=False)
    currency = DB.Column(DB.String(3), nullable=False)
    # deadline = DB.Column(DB.DateTime, nullable=False)
    goal = DB.Column(DB.Float, nullable=False)
    # launched = DB.Column(DB.DateTime, nullable=False)
    pledged = DB.Column(DB.Float, nullable=False)
    backers = DB.Column(DB.Integer, nullable=False)
    country = DB.Column(DB.String(10), nullable=False)
    usd_pledged = DB.Column(DB.Float, nullable=False)
    usd_pledged_real = DB.Column(DB.Float, nullable=False)
    usd_goal_real = DB.Column(DB.Float, nullable=False)
    days = DB.Column(DB.Integer, nullable=False)

    def __repr__(self):
        return 'Project Name {}'.format(self.project_name)
