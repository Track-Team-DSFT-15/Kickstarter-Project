import numpy as np
from sklearn.linear_model import LogisticRegression
from .models import User, DB
import pandas as pd
# import pickle
# import .kevin_model
# from NN_model import m
from tensorflow.keras.models import load_model
import numpy as np

def predict_user():
    dict = {col.name: [getattr(User.query.all()[-1], str(col.name))] for col in User.__table__.columns}
    df = pd.DataFrame(dict).set_index('id')
    # df = df.to_numpy()
    # df = [5000, 94175, 761, 121857.33, 6469.73]
    df = df.values.tolist()
    # df = pd.DataFrame(columns=['project_name', 'category', 'main_category',
    #                                'currency', 'deadline', 'goal', 'launched',
    #                                'pledged', 'backers', 'country', 'usd_pledged',
    #                                'usd_pledged_real', 'usd_goal_real'])
    # dictionary = User.query.all()[-1].__dict__
    # df = df.append(dictionary, ignore_index=True)
    reconstructed_model = load_model('kevin_model')
    return str(reconstructed_model.predict(df, batch_size=10))
