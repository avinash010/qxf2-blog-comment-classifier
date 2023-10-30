"""
Figure out if a message is Spam or not a spam
"""
import os
import pickle
import pandas as pd
import preprocess_message as message_cleaner

CURRENT_DIRECTORY = os.path.dirname(__file__)
MODEL_FILENAME = os.path.join(CURRENT_DIRECTORY, 'comment_classifier.pickle')
COMMENT_FILENAME = os.path.join(CURRENT_DIRECTORY,'comments.log')

def get_model():
    "Return the model"
    return pickle.load(open(MODEL_FILENAME, 'rb'))

def store_message(message,answer):
    "Store the input message to file for analysis at a later time"
    with open(COMMENT_FILENAME,'a') as file_handler:
        file_handler.write(f"{message},{answer}\n")

def is_this_a_spam(message):
    "Return a prediction of whether this is Spam or not a spam message"
    answer = 0
    model = get_model()
    preprocessed_message = message_cleaner.preprocess_data(message)  # Preprocess the message
    answer = model.predict([preprocessed_message])[0]
    store_message(preprocessed_message,answer)

    return answer

if __name__ == "__main__":
    Answer = is_this_a_spam("casinosa")
    print(Answer)
