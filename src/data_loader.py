import pandas as pd
import streamlit as st

def load_processed_data(filepath='data/processed/cleaned_sentiment_data.csv'):
    """
    Loads the pre-processed and sentiment-analyzed data from a CSV file.

    Args:
        filepath (str): The path to the processed CSV file.

    Returns:
        pandas.DataFrame: A DataFrame containing the loaded data, or None if an error occurs.
    """
    try:
        df = pd.read_csv(filepath, parse_dates=['date'])
        return df
    except FileNotFoundError:
        st.error(f"Error: The processed data file was not found at '{filepath}'.")
        st.warning("Please ensure you have run the data processing notebooks first, or that the file is in the correct directory.")
        return None
    except Exception as e:
        st.error(f"An error occurred while loading the processed data: {e}")
        return None

