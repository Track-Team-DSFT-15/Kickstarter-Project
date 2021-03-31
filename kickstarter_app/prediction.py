import numpy as np
from sklearn.linear_model import LogisticRegression
from .models import User, DB
import pandas as pd
import joblib
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow import keras




def predict_user():
    dict = {col.name: [getattr(User.query.all()[0], str(col.name))] for col in User.__table__.columns}
    df = pd.DataFrame(dict).set_index('id')
    # df = pd.DataFrame(columns=['project_name', 'category', 'main_category',
    #                                'currency', 'deadline', 'goal', 'launched',
    #                                'pledged', 'backers', 'country', 'usd_pledged',
    #                                'usd_pledged_real', 'usd_goal_real'])
    # dictionary = User.query.all()[-1].__dict__
    # df = df.append(dictionary, ignore_index=True)
    loaded_model = joblib.load('kickstarter_nn_model')
    # loaded_model = keras.models.load_model('kickstarter_app/kickstarter_nn_model')
    return str(loaded_model.predict(df, batch_size=10))
