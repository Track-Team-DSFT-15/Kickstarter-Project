import numpy as np
from sklearn.linear_model import LogisticRegression
from .models import User, DB


def predict_user(df):
    df = pd.DataFrame(columns=['project_name', 'category', 'main_category',
                                   'currency', 'deadline', 'goal', 'launched',
                                   'pledged', 'backers', 'country', 'usd_pledged',
                                   'usd_pledged_real', 'usd_goal_real'])
    dictionary = User.query.all()[0].__dict__
    df = df.append(dictionary, ignore_index=True)

    model = (model_de_kevin.fit)
    return str(model.predict(df))
