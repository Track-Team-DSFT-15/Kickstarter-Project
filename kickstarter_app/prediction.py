import numpy as np
from sklearn.linear_model import LogisticRegression
from .models import User, DB
import pandas as pd
import pickle
from NN_model import m



def predict_user():
    dict = {col.name: [getattr(User.query.all()[0], str(col.name))] for col in User.__table__.columns}
    df = pd.DataFrame(dict).set_index('id')
    # df = pd.DataFrame(columns=['project_name', 'category', 'main_category',
    #                                'currency', 'deadline', 'goal', 'launched',
    #                                'pledged', 'backers', 'country', 'usd_pledged',
    #                                'usd_pledged_real', 'usd_goal_real'])
    # dictionary = User.query.all()[-1].__dict__
    # df = df.append(dictionary, ignore_index=True)
    loaded_model = pickle.load(open('test_model', 'rb'))
    return str(loaded_model.evaluate(df))
