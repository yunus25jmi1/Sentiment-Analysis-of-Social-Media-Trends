from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the analyzer once when the module is loaded
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment_vader(df, text_column='processed_text'):
    """
    Analyzes the sentiment of text in a DataFrame column using VADER.

    Args:
        df (pandas.DataFrame): The DataFrame containing the text data.
        text_column (str): The name of the column with the text to analyze.

    Returns:
        pandas.DataFrame: The original DataFrame with two new columns:
                          'vader_score' and 'vader_label'.
    """
    # Get VADER compound score
    df['vader_score'] = df[text_column].apply(
        lambda text: analyzer.polarity_scores(text)['compound']
    )

    # Categorize the score
    df['vader_label'] = df['vader_score'].apply(categorize_sentiment)
    
    return df

def categorize_sentiment(score):
    """
    Categorizes a VADER sentiment score into Positive, Negative, or Neutral.

    Args:
        score (float): The VADER compound score (-1 to 1).

    Returns:
        str: The sentiment label ('Positive', 'Negative', 'Neutral').
    """
    if score > 0.05:
        return 'Positive'
    elif score < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

