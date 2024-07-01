from inference_engine import InferenceEngine
from ml_model import train_ml_model

def main():
    print("\n\n+-------------------------------------------------------------+")
    print("+---- Welcome to the Educational Counseling Chatbot! ---------+")
    print("+-------------------------------------------------------------+\n")
    print("+---- Developed By:")
    print("+--------> Akila Dilan (E223739)")
    print("+--------> Sheleena Johnson (E024849)\n")
    print("+-------------------------------------------------------------+\n")
    print("Initializing Chatbot ...\n")

    engine = InferenceEngine()

    print("\nInitialization Completed ...\n")

    # Train the ML model from logged interactions
    ml_model = train_ml_model()
    print("> Model is trained and ready to use.\n")
    engine.set_ml_model(ml_model)

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = engine.get_response(user_input)
        print(f"\nCounsellor: \n{response}")

if __name__ == "__main__":
    main()
