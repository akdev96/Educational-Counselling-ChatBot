import sqlite3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from nltk.corpus import stopwords
import nltk

# Ensure that the NLTK stopwords are downloaded
nltk.download('stopwords')

class MLModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = SGDClassifier()

    def train(self, user_inputs, bot_responses):
        stop_words = set(stopwords.words('english'))
        # Clean the data
        user_inputs = user_inputs.apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in stop_words]))
        # Remove empty entries
        user_inputs = user_inputs[user_inputs.str.strip() != '']
        bot_responses = bot_responses.loc[user_inputs.index]

        if user_inputs.empty:
            raise ValueError("Training data is empty after cleaning. Please provide valid training data.")

        print("> Starting training process...")
        X = self.vectorizer.fit_transform(user_inputs)
        self.model.fit(X, bot_responses)
        print("> Training completed.")

    def predict(self, user_input):
        X = self.vectorizer.transform([user_input])
        return self.model.predict(X)[0]

def train_ml_model():
    conn = sqlite3.connect('education_counseling.db')
    df = pd.read_sql_query("SELECT user_input, bot_response FROM user_interactions", conn)
    conn.close()

    if df.empty:
        raise ValueError("No data found in the database for training.")

    ml_model = MLModel()
    ml_model.train(df['user_input'], df['bot_response'])
    return ml_model
