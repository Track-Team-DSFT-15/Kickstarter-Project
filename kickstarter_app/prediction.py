import numpy as np
from sklearn.linear_model import LogisticRegression
from .models import User, DB
from .twitter import vectorize_tweet


def predict_user(username_1, username_2, hypo_tweet):
    """
    Determines who is more likely to say a tweet.

    Returns a zero or one depending on who is more likely to say the
    hypothetical tweet. One is corresponding to username_1 and zero corresponds to username_2.
    """
    user1 = User.query.filter(User.username == username_1).one()
    user2 = User.query.filter(User.username == username_2).one()

    user1_stacked_embeddings = np.array([])
    for embedding in user1.embeddings:
        user1_stacked_embeddings = np.vstack(
            user1_stacked_embeddings, embedding)

    user2_stacked_embeddings = np.array([])
    for embedding in user2.embeddings:
        user2_stacked_embeddings = np.vstack(
            user2_stacked_embeddings, embedding)

    embeddings = np.vstack(user1_stacked_embeddings, user2_stacked_embeddings)

    labels = np.concatenate(
        [np.zeros(len(user1.embeddings)), np.ones(len(user2.embeddings))])

    log_reg = LogisticRegression().fit(embeddings, labels)

    tweet_embedding = vectorize_tweet(hypo_tweet)
    return log_reg.predict(np.array(tweet_embedding).reshape(1, -1))
