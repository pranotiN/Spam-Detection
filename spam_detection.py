
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

def load_data(filepath):
    """Loads data from a CSV file into a pandas DataFrame."""
    return pd.read_csv(filepath, encoding='latin-1')

def prepare_data(df):
    """Prepares the data for training."""
    df['label'] = df['v1'].map({'ham': 0, 'spam': 1})
    X = df['v2']
    y = df['label']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def create_model():
    """Creates a Naive Bayes classifier pipeline."""
    return make_pipeline(CountVectorizer(), MultinomialNB())

def train_model(model, X_train, y_train):
    """Trains the model."""
    model.fit(X_train, y_train)

def save_model(model, filepath):
    """Saves the trained model to a file."""
    joblib.dump(model, filepath)

def load_model(filepath):
    """Loads a trained model from a file."""
    return joblib.load(filepath)
