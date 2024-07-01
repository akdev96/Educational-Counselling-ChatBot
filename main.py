from inference_engine import InferenceEngine

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

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = engine.get_response(user_input)
        print(f"Counsellor: \n{response}")

if __name__ == "__main__":
    main()
