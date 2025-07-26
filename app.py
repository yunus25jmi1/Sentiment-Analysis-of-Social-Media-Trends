import streamlit as st
import pandas as pd

# Import the functions from our source code modules
from src.data_loader import load_processed_data
from src.visualizer import (
    plot_sentiment_over_time,
    plot_sentiment_distribution,
    generate_word_clouds
)

def main():
    """
    Main function to run the Streamlit application.
    """
    st.set_page_config(page_title="Social Media Sentiment Analyzer", layout="wide")

    # --- Main Panel ---
    st.title("📈 Social Media Trend Sentiment Analyzer")
    st.markdown("""
        Welcome to the Sentiment Analyzer! This dashboard visualizes the sentiment of a pre-loaded
        social media dataset about various topics.
        
        **What you're seeing:**
        1.  **Sentiment Over Time:** A line chart showing the daily average sentiment score.
        2.  **Overall Distribution:** A donut chart breaking down the posts into Positive, Negative, and Neutral categories.
        3.  **Key Metrics & Word Clouds:** High-level statistics and the most common words associated with positive and negative sentiments.
    """)

    # --- Load Data ---
    # For the hackathon, we load our pre-processed data directly for speed and reliability.
    # The file uploader logic from the initial prototype has been removed to focus on this core analysis.
    analyzed_df = load_processed_data()

    if analyzed_df is not None:
        st.success(f"Successfully loaded and analyzed {len(analyzed_df):,} records.")

        # --- Display Visualizations ---
        st.header("📊 Analysis Dashboard")
        
        # 1. Time Series Plot
        time_series_chart = plot_sentiment_over_time(analyzed_df.copy())
        st.altair_chart(time_series_chart, use_container_width=True)
        st.divider()
        
        # 2. Distribution and Metrics
        col1, col2 = st.columns([1, 2], gap="large")
        with col1:
            dist_chart = plot_sentiment_distribution(analyzed_df)
            st.altair_chart(dist_chart, use_container_width=True)
        
        with col2:
            st.subheader("Key Metrics")
            avg_sentiment = analyzed_df['vader_score'].mean()
            positive_pct = (analyzed_df['vader_label'] == 'Positive').sum() / len(analyzed_df) * 100
            negative_pct = (analyzed_df['vader_label'] == 'Negative').sum() / len(analyzed_df) * 100
            
            st.metric("Average Sentiment Score", f"{avg_sentiment:.3f}", 
                      help="The average VADER compound score across all posts. Ranges from -1 (most negative) to +1 (most positive).")
            st.metric("Positive Posts", f"{positive_pct:.1f}%")
            st.metric("Negative Posts", f"{negative_pct:.1f}%")

        st.divider()

        # 3. Word Clouds
        st.header("💬 Most Common Words")
        with st.spinner("Generating word clouds..."):
            word_cloud_fig = generate_word_clouds(analyzed_df)
            st.pyplot(word_cloud_fig)
            
        # Optional: Display a sample of the data
        with st.expander("View Processed Data Sample"):
            st.dataframe(analyzed_df[['date', 'text', 'vader_score', 'vader_label']].head(10))

    else:
        st.error("Could not load the dataset. Please ensure the file 'data/processed/cleaned_sentiment_data.csv' exists.")


if __name__ == "__main__":
    main()
