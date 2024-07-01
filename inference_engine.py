import nltk
from nltk.tokenize import word_tokenize
from datetime import datetime
from database import Database

class InferenceEngine:
    def __init__(self):
        self.static_responses = {
            "hello": "Hi there! How can I assist you today?",
            "hi": "Hi there! How can I assist you today?",
            "thank you": "You're welcome!"
        }
        nltk.download('punkt')
        self.db = Database()
        self.db.create_log_table()
        self.db.create_courses_table()

    def log_interaction(self, user_input, bot_response):
        self.db.log_interaction(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_input, bot_response)

    def get_response(self, user_input):
        # Simple rule-based logic
        if user_input.lower() in self.static_responses:
            response = self.static_responses[user_input.lower()]
            self.log_interaction(user_input, response)
            return response

        # NLTK processing
        tokens = word_tokenize(user_input.lower())
        response = self.query_database(tokens)
        if response:
            self.log_interaction(user_input, response)
            return response

        response = "I'm not sure how to help with that. Can you please provide more details?"
        self.log_interaction(user_input, response)
        return response

    def query_database(self, tokens):
        if "courses" in tokens:
            results = self.db.get_courses()
            return '\n'.join([f"{name}: {details}" for name, details in results]) if results else "No courses available."
        return None

    def update_knowledge_base(self, course_name, course_details):
        self.db.insert_course(course_name, course_details)
