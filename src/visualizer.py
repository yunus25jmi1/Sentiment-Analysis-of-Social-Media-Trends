import pandas as pd
import altair as alt
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def plot_sentiment_over_time(df):
    """
    Generates an interactive Altair line chart of sentiment over time.

    Args:
        df (pandas.DataFrame): DataFrame with 'date' and 'vader_score' columns.

    Returns:
        altair.Chart: The Altair chart object.
    """
    # Resample by day to get the mean sentiment score
    daily_sentiment = df.set_index('date')['vader_score'].resample('D').mean().reset_index()

    chart = alt.Chart(daily_sentiment).mark_line(
        point=alt.OverlayMarkDef(color="red", size=20, filled=False),
        strokeWidth=2
    ).encode(
        x=alt.X('date:T', title='Date'),
        y=alt.Y('vader_score:Q', title='Average Sentiment Score', scale=alt.Scale(zero=False)),
        tooltip=[
            alt.Tooltip('date:T', title='Date'),
            alt.Tooltip('vader_score:Q', title='Avg. Score', format='.3f')
        ]
    ).properties(
        title='Daily Average Sentiment Trend'
    ).interactive()
    
    return chart

def plot_sentiment_distribution(df):
    """
    Generates an Altair donut chart of the overall sentiment distribution.

    Args:
        df (pandas.DataFrame): DataFrame with a 'vader_label' column.

    Returns:
        altair.Chart: The Altair chart object.
    """
    sentiment_counts = df['vader_label'].value_counts().reset_index()
    sentiment_counts.columns = ['vader_label', 'count']

    chart = alt.Chart(sentiment_counts).mark_arc(
        innerRadius=60,
        outerRadius=110
    ).encode(
        theta=alt.Theta(field="count", type="quantitative"),
        color=alt.Color(field="vader_label", type="nominal",
                        scale=alt.Scale(
                            domain=['Positive', 'Negative', 'Neutral'],
                            range=['#2ca02c', '#d62728', '#ff7f0e'] # Green, Red, Orange
                        ),
                        legend=alt.Legend(title="Sentiment")),
        tooltip=['vader_label', 'count']
    ).properties(
        title='Overall Sentiment Distribution'
    )
    
    return chart

def generate_word_clouds(df):
    """
    Generates and displays word clouds for positive and negative sentiment.

    Args:
        df (pandas.DataFrame): DataFrame with 'processed_text' and 'vader_label' columns.

    Returns:
        matplotlib.figure.Figure: The figure object containing the word cloud plots.
    """
    positive_text = " ".join(text for text in df[df['vader_label'] == 'Positive']['processed_text'] if isinstance(text, str))
    negative_text = " ".join(text for text in df[df['vader_label'] == 'Negative']['processed_text'] if isinstance(text, str))

    # Create figure for plotting
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))
    
    # Positive Word Cloud
    if positive_text:
        wc_positive = WordCloud(width=800, height=400, background_color='white', colormap='Greens').generate(positive_text)
        axes[0].imshow(wc_positive, interpolation='bilinear')
        axes[0].set_title('Most Common Words in Positive Posts', fontsize=14)
    else:
        axes[0].text(0.5, 0.5, 'No positive text found.', ha='center', va='center')
    axes[0].axis('off')

    # Negative Word Cloud
    if negative_text:
        wc_negative = WordCloud(width=800, height=400, background_color='white', colormap='Reds').generate(negative_text)
        axes[1].imshow(wc_negative, interpolation='bilinear')
        axes[1].set_title('Most Common Words in Negative Posts', fontsize=14)
    else:
        axes[1].text(0.5, 0.5, 'No negative text found.', ha='center', va='center')
    axes[1].axis('off')
    
    plt.tight_layout(pad=0)
    return fig

