from ml_model import MLModel, train_ml_model

if __name__ == "__main__":
    # Train the ML model
    ml_model = train_ml_model()

    # Example predictions
    test_input = "What courses do you offer?"
    prediction = ml_model.predict(test_input)
    print(f"Prediction: {prediction}")

    test_input = "How much does the Computer Science course cost?"
    prediction = ml_model.predict(test_input)
    print(f"Prediction: {prediction}")
