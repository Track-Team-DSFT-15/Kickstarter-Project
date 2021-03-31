import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential, save_model, load_model, Model
from tensorflow.keras.layers import Dense
from zip_unpack import zf
import pickle
import types
import tempfile


# Define the numeric features

numeric_features = ['ID', 'goal', 'pledged', 'backers',
                    'usd pledged','usd_pledged_real', 'usd_goal_real']


# Define the categorical features

categorical_features = ['name', 'category', 'main_category', 'currency', 'country', 'state']

past_campaigns = pd.read_csv(zf.open('ks-projects-201801.csv.zip'))
past_campaigns_numeric = pd.read_csv(zf.open('ks-projects-201801.csv.zip'), usecols=numeric_features)
past_campaigns_categorical = pd.read_csv(zf.open('ks-projects-201801.csv.zip'), usecols=categorical_features)
past_campaigns_numeric_dropped = past_campaigns_numeric.drop(labels=['ID','usd pledged'], axis=1)
X = past_campaigns_numeric_dropped


def categorize_success(state):
  if state in ['failed','canceled', 'undefined', 'suspended']:
    return False
  else:
    return  True


past_campaigns_categorical['success'] = past_campaigns_categorical['state'].apply(categorize_success)
y = past_campaigns_categorical['success']


# Create the training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


# Define the keras model
model = Sequential()
# Expand nodes in hidden layer inverse to input dimensionality
model.add(Dense(250, input_dim=(5), activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(1, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))


model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model.fit(X, y, epochs=10, batch_size=10, verbose=0);

print('Model accuracy: ', model.evaluate(X, y)[1]*100)

model.save('kevin_model')
