"""
Preprocess incoming message to match what the training model uses
a)Mimic the training model - stem the words
"""
from nltk.stem import SnowballStemmer


def preprocess_data(input_data):
    """Preprocess the data, including text cleaning and stemming."""
    # Initialize the SnowballStemmer
    stemmer = SnowballStemmer("english")
    # Split the input string into words and apply stemming
    words = input_data.split()
    stemmed_words = [stemmer.stem(word) for word in words]
    # Join the stemmed words back into a string
    preprocessed_data = " ".join(stemmed_words)
    return preprocessed_data

