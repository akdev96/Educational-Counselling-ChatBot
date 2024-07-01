import sqlite3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier

class MLModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = SGDClassifier()

    def train(self, user_inputs, bot_responses):
        X = self.vectorizer.fit_transform(user_inputs)
        self.model.fit(X, bot_responses)

    def predict(self, user_input):
        X = self.vectorizer.transform([user_input])
        return self.model.predict(X)[0]

def train_ml_model():
    conn = sqlite3.connect('education_counseling.db')
    df = pd.read_sql_query("SELECT user_input, bot_response FROM user_interactions", conn)
    conn.close()

    ml_model = MLModel()
    ml_model.train(df['user_input'], df['bot_response'])
    return ml_model
