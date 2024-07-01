import sqlite3
from datetime import datetime
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
import nltk
from nltk.corpus import stopwords

# Ensure NLTK resources are downloaded
nltk.download('stopwords')

# Database Setup (SQLite)
def setup_database():
    # Connect to SQLite database
    conn = sqlite3.connect('education_counseling.db')
    c = conn.cursor()

    # Create table for courses
    c.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY,
        name TEXT,
        course TEXT,
        requirement TEXT,
        price TEXT,
        offering_university TEXT
    )
    ''')

    # Create table for user interactions
    c.execute('''
    CREATE TABLE IF NOT EXISTS user_interactions (
        id INTEGER PRIMARY KEY,
        timestamp TEXT,
        user_input TEXT,
        bot_response TEXT
    )
    ''')

    # Insert sample data (if needed)
    c.execute("INSERT INTO courses (name, course, requirement, price, offering_university) VALUES ('Computer Science', 'B.Sc. in Computer Science', 'High School Diploma', '10000', 'University A')")
    c.execute("INSERT INTO courses (name, course, requirement, price, offering_university) VALUES ('Business Administration', 'BBA in Business Administration', 'High School Diploma', '8000', 'University B')")

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

# Function to fetch course information
def fetch_courses():
    # Connect to SQLite database
    conn = sqlite3.connect('education_counseling.db')
    c = conn.cursor()

    # Fetch all courses
    c.execute("SELECT name, course, requirement, price, offering_university FROM courses")
    courses = c.fetchall()

    # Close the connection
    conn.close()

    # Format the result for display
    if courses:
        response = "Here are the courses we offer:\n"
        for course in courses:
            response += f"\nName: {course[0]}\nDetails: {course[1]}\nRequirement: {course[2]}\nPrice: {course[3]}\nOffering University: {course[4]}\n"
        return response
    else:
        return "No courses available."

# Function to log user interactions
def log_interaction(user_input, bot_response):
    # Connect to SQLite database
    conn = sqlite3.connect('education_counseling.db')
    c = conn.cursor()

    # Insert the interaction log
    c.execute('''
    INSERT INTO user_interactions (timestamp, user_input, bot_response) 
    VALUES (?, ?, ?)
    ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_input, bot_response))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

# Function to fetch logged interactions for ML training
def fetch_logged_interactions():
    # Connect to SQLite database
    conn = sqlite3.connect('education_counseling.db')
    
    # Read logged interactions into a DataFrame
    df = pd.read_sql_query("SELECT user_input, bot_response FROM user_interactions", conn)
    
    # Close the connection
    conn.close()

    return df

# ML Model class
class MLModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
        self.model = SGDClassifier()

    def train(self, user_inputs, bot_responses):
        if user_inputs.empty:
            raise ValueError("Training data is empty. Ensure there are logged interactions for training.")

        X = self.vectorizer.fit_transform(user_inputs)
        self.model.fit(X, bot_responses)

    def predict(self, user_input):
        X = self.vectorizer.transform([user_input])
        return self.model.predict(X)[0]

# Function to train the ML model
def train_ml_model():
    df = fetch_logged_interactions()

    ml_model = MLModel()
    ml_model.train(df['user_input'], df['bot_response'])
    return ml_model

# Example usage
if __name__ == "__main__":
    # Setup database (if not already setup)
    setup_database()

    # Example user input and fetching courses
    user_input = "What courses do you offer?"
    bot_response = fetch_courses()
    print(bot_response)

    # Log the interaction
    log_interaction(user_input, bot_response)

    # Train the ML model from logged interactions
    ml_model = train_ml_model()

    # Example predictions
    test_input = "How much does the Computer Science course cost?"
    prediction = ml_model.predict(test_input)
    print(f"Prediction: {prediction}")
