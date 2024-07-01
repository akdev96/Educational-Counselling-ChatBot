# Inference Engine with NLTK
import nltk
from nltk.tokenize import word_tokenize

class InferenceEngine:
    def __init__(self):
        self.static_responses = {
            "hello": "Hi there! How can I assist you today?",
            "thank you": "You're welcome!"
        }
        nltk.download('punkt')

    def get_response(self, user_input):
        # Simple rule-based logic
        if user_input.lower() in self.static_responses:
            return self.static_responses[user_input.lower()]

        # NLTK processing
        tokens = word_tokenize(user_input.lower())
        response = self.query_database(tokens)
        if response:
            return response
        return "I'm not sure how to help with that. Can you please provide more details?"

    def query_database(self, tokens):
        import sqlite3
        conn = sqlite3.connect('education_counseling.db')
        c = conn.cursor()

        if "courses" in tokens:
            c.execute("SELECT name, details FROM courses")
            results = c.fetchall()
            conn.close()
            return '\n'.join([f"{name}: {details}" for name, details in results]) if results else "No courses available."
        return None

# Natural Language Interface (CLI)
def main():
    print("Welcome to the Educational Counseling Chatbot!\n")
    engine = InferenceEngine()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = engine.get_response(user_input)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()
