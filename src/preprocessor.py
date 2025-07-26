import re
import nltk
from nltk.corpus import stopwords

# Ensure stopwords are available
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    """
    Cleans and preprocesses a single piece of text by removing URLs, mentions,
    punctuation, converting to lowercase, and removing stopwords.

    Args:
        text (str): The raw text string.

    Returns:
        str: The cleaned text string.
    """
    if not isinstance(text, str):
        return ""
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove user @ references and '#' from hashtags
    text = re.sub(r'\@\w+|\#','', text)
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Convert to lower case
    text = text.lower()
    # Remove stopwords
    text_tokens = text.split()
    filtered_words = [word for word in text_tokens if word not in stop_words]
    
    return " ".join(filtered_words)

