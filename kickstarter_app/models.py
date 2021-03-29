from flask_sqlalchemy import SQLAlchemy

# Creating DB
DB = SQLAlchemy()


# Creating a user table
class User(DB.Model):
    """Stores Twitter users and corresponding tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    username = DB.Column(DB.String(50), nullable=False)
    fullname = DB.Column(DB.String(50), nullable=False)
    tweets_text = DB.Column(DB.PickleType)
    embeddings = DB.Column(DB.PickleType)

    def __repr__(self):
        return "<User {}>".format(self.fullname)
