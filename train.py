
from spam_detection import load_data, prepare_data, create_model, train_model, save_model

# File path for the dataset
DATA_FILEPATH = 'spam.csv'
# File path for the saved model
MODEL_FILEPATH = 'spam_model.joblib'

def main():
    """Trains the spam detection model and saves it."""
    print(f"Loading data from {DATA_FILEPATH}...")
    df = load_data(DATA_FILEPATH)
    
    print("Preparing data...")
    X_train, _, y_train, _ = prepare_data(df)
    
    print("Creating and training the model...")
    model = create_model()
    train_model(model, X_train, y_train)
    
    print(f"Saving the model to {MODEL_FILEPATH}...")
    save_model(model, MODEL_FILEPATH)
    
    print("Model training complete.")

if __name__ == '__main__':
    main()
