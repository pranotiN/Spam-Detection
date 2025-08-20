
import sys
from spam_detection import load_model

# File path for the saved model
MODEL_FILEPATH = 'spam_model.joblib'

def predict_message(message):
    """Predicts whether a message is spam or not."""
    model = load_model(MODEL_FILEPATH)
    prediction = model.predict([message])
    return 'spam' if prediction[0] == 1 else 'ham'

def main():
    """Loads the model and predicts the class of a new message."""
    if len(sys.argv) < 2:
        print("Usage: python predict.py <message>")
        sys.exit(1)
    
    message = sys.argv[1]
    prediction = predict_message(message)
    print(f'The message is predicted to be: {prediction}')

if __name__ == '__main__':
    main()
