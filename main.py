import nltk
from nltk.tokenize import word_tokenize

#class InferenceEngine:
    # Interface Code Here
        
      

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
