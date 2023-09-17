import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# Initialize the VADER sentiment intensity analyzer
analyzer = SentimentIntensityAnalyzer()

# Load the data from the Excel file
english_texts_df = pd.read_excel('english_texts.xlsx')

st.markdown(
    """
    <style>
        .title {
            font-size: 72px;
            font-weight: bold;
            color: yellow;
        }
        .subtitle {
            font-size: 72px;
            font-weight: bold;
            color: black;
        }
        .stButton > button {
                        color: black;
                        border: 3px solid yellow;
                        font-size: 18px;
                        padding: 10px 20px;
                        width: auto;
                        height: auto;
                    }

        .big-title {
            font-size: 28px;
        }
    </style>
    """, unsafe_allow_html=True
)

st.markdown(
    """
    <span class="title">One</span><span class="subtitle">AMZ</span>
    """, unsafe_allow_html=True
)

st.markdown('<p class="big-title">Duygu Analizi</p>', unsafe_allow_html=True)

# Dropdown to choose text
selected_text = st.selectbox("**OneAMZ yorumlarından bir tane seçin**", english_texts_df['english_texts'].tolist())
user_input = st.text_area("**Lütfen bir tane yorum yazın**", selected_text)

if st.button('ANALİZ'):
    score = analyzer.polarity_scores(user_input)
    if -0.05 < score['compound'] < 0.05:
        result = 'Neutral'
    elif score['compound'] > 0:
        result = 'Positive'
    else:
        result = 'Negative'
    st.write(f"The sentiment is: **{result}**")

