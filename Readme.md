
# 📈 Social Media Trend Sentiment Analyzer

**Hackathon:** Data Hackfest 2025  
**Project Link:** [GitHub Repository](https://github.com/yunus25jmi1/Sentiment-Analysis-of-Social-Media-Trends)  
**Devpost Link:** [Devpost Submission](https://devpost.com/software/social-media-trend-sentiment-analyzer)  
**Deployed Link:** [Live Demo](https://sentiment-analysis-of-social-media-trends.onrender.com)

---

## 🚀 Project Overview

In today's fast-paced digital world, public opinion can shift in an instant. The **Social Media Trend Sentiment Analyzer** is a powerful yet intuitive web application designed to capture and visualize the collective mood of social media conversations. By processing and analyzing a large dataset of tweets, this tool provides at-a-glance insights into public sentiment, helping users understand not just *if* a trend is positive or negative, but *why*.

This project demonstrates an **end-to-end data science workflow**, from data cleaning and NLP-based sentiment analysis to the development of an interactive and insightful user dashboard.

---

## ✨ Key Features

* **Automated NLP Pipeline:** Implements a robust text preprocessing pipeline to clean raw social media text, removing noise like URLs, mentions, and stopwords.
* **Accurate Sentiment Analysis:** Utilizes the **VADER (Valence Aware Dictionary and sEntiment Reasoner)** model, which is specifically tuned for social media language, slang, and emojis, to accurately classify each post as **Positive**, **Negative**, or **Neutral**.
* **Interactive Time-Series Analysis:** A dynamic line chart visualizes the average sentiment score over time, allowing users to pinpoint key dates where public opinion changed.
* **At-a-Glance Distribution:** A clean donut chart provides an immediate summary of the overall sentiment proportions across the entire dataset.
* **Contextual Word Clouds:** To understand the "why" behind the sentiment, the dashboard generates separate word clouds for positive and negative posts, highlighting the specific terms and topics driving the conversation.
* **Modular & Scalable Codebase:** The project is built with a clean, modular structure, separating data loading, visualization, and application logic for easy maintenance and future expansion.

---

## 📊 Potential Findings & Insights

Using this dashboard on a dataset of tweets, a user could quickly discover insights such as:

* A sharp dip in sentiment on a specific day, correlating with a product's buggy update release.
* The word "amazing" and "fast" appearing prominently in the positive word cloud, indicating users value performance.
* The word "support" and "wait" appearing in the negative word cloud, highlighting issues with customer service.
* A gradual increase in positive sentiment over a month, suggesting a successful marketing campaign.

---

## 🛠️ Technologies & Libraries

* **Backend & Web Framework:** Python, Streamlit
* **Data Manipulation & Analysis:** Pandas, NumPy
* **NLP & Sentiment Analysis:** NLTK (Natural Language Toolkit), VADER
* **Data Visualization:** Altair, Matplotlib, WordCloud

---

## ⚙️ Setup and Usage

Follow these steps to get the application running on your local machine.

### 1. Prerequisites

* Python 3.8+
* `pip` package manager

### 2. Clone the Repository

```bash
git clone https://github.com/yunus25jmi1/Sentiment-Analysis-of-Social-Media-Trends.git
cd Sentiment-Analysis-of-Social-Media-Trends
````

### 3\. Create a Virtual Environment (Recommended)

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### 4\. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5\. Generate the Processed Data

The app runs on pre-processed data for speed. **You must generate this file first.**

1.  **Download the data:** Get the raw dataset (e.g., from Kaggle) and place it in the `data/raw/` folder.
2.  **Run the processing notebook:** Open and run all cells in `notebooks/02_preprocessing_analysis.ipynb`. This will create the necessary `cleaned_sentiment_data.csv` file in the `data/processed/` directory.

### 6\. Run the Application

Launch the Streamlit app with the following command. Make sure your virtual environment is active\!

```bash
streamlit run app.py
```

Your web browser will open with the interactive dashboard.

-----

*This project was proudly developed for the Data Hackfest 2025.*
