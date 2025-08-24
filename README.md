# Spam Detection POC

This is a proof-of-concept for a spam detection application using Python and scikit-learn.

## Project Structure

*   `spam_detection.py`: Contains the core functions for loading data, preparing it, creating the model, and saving/loading the model.
*   `train.py`: Trains the spam detection model using the data in `spam.csv` and saves the trained model to `spam_model.joblib`.
*   `predict.py`: Uses the trained model to predict whether a given message is spam or ham.
*   `requirements.txt`: Lists the Python dependencies for this project.
*   `spam.csv`: A small dataset of SMS messages labeled as spam or ham.
*   `.gitignore`: Specifies which files and directories to ignore in the git repository.

## How to Run

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/pranotiN/Spam-Detection.git
    cd Spam-Detection
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    or
     ```bash
    python3 -m pip install -r requirements.txt
      ```

4.  **Train the model:**

    ```bash
    python3 train.py
    ```

5.  **Make predictions:**

    ```bash
    python3 predict.py "Your message here"
    ```

    For example:

    ```bash
    python3 predict.py "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's"
    ```

    This will output:

    ```
    The message is predicted to be: spam
    ```
