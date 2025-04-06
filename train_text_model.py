import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import re
from wordcloud import WordCloud

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

import preprocess_kgptalkie as ps
import gensim

fake = pd.read_csv('https://raw.githubusercontent.com/laxmimerit/fake-real-news-dataset/main/data/Fake.csv')
real = pd.read_csv('https://raw.githubusercontent.com/laxmimerit/fake-real-news-dataset/main/data/True.csv')

# Handle missing, merge title + text, lowercase, etc.

real['text'] = real['title'] + " " + real['text']
fake['text'] = fake['title'] + " " + fake['text']

real['text'] = real['text'].apply(lambda x : str(x).lower())
fake['text'] = fake['text'].apply(lambda x : str(x).lower())

real['class'] = 1
fake['class'] = 0

real = real[['text', 'class']]
fake = fake[['text', 'class']]

data = pd.concat([real, fake], ignore_index=True)
data['text'] = data['text'].apply(lambda x: ps.remove_special_chars(x))

y = data['class'].values
X = [d.split() for d in data['text'].tolist()]

DIM = 100
w2v_model = gensim.models.Word2Vec(sentences=X, vector_size=DIM, window=10, min_count=1)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(X)
X = tokenizer.texts_to_sequences(X)

maxlen = 1000
X = pad_sequences(X, maxlen=maxlen)

vocab_size = len(tokenizer.word_index) + 1
vocab = tokenizer.word_index

def get_weight_matrix(model, vocab, vocab_size, DIM):
    weight_matrix = np.zeros((vocab_size, DIM))
    for word, i in vocab.items():
        if word in model.wv:
            weight_matrix[i] = model.wv[word]
    return weight_matrix

embedding_vectors = get_weight_matrix(w2v_model, vocab, vocab_size, DIM)

model = Sequential()
model.add(Embedding(vocab_size, output_dim=DIM, weights=[embedding_vectors], input_length=maxlen, trainable=False))
model.add(LSTM(units=128))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(X_train, y_train, validation_split=0.3, epochs=6)

y_pred = (model.predict(X_test) >= 0.5).astype(int)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

model.save("text_detector_model.h5")

# Also save tokenizer
import pickle
with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)









GOOGLE_FACT_CHECK_API_KEY = 'AIzaSyCaxgI1rS_BiYJZGuOqE5usisbVN_Yh864'
NEWSAPI_KEY = '77f6e51c9d634b36a75d665c285a4ff3'

import requests

def verify_with_google_fact_check(claim):
    url = f"https://factchecktools.googleapis.com/v1alpha1/claims:search"
    params = {
        'query': claim,
        'key': GOOGLE_FACT_CHECK_API_KEY,
        'languageCode': 'en'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        result = response.json().get('claims', [])
        return result
    else:
        print("Error from Google Fact Check API:", response.text)
        return []

def fetch_news_sources(claim):
    url = f"https://newsapi.org/v2/everything"
    params = {
        'q': claim,
        'apiKey': NEWSAPI_KEY,
        'language': 'en',
        'sortBy': 'relevancy',
        'pageSize': 5
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return articles
    else:
        print("Error from NewsAPI:", response.text)
        return []

import requests

# -----------------------------
# Configuration
# -----------------------------
NEWS_API_KEY = "77f6e51c9d634b36a75d665c285a4ff3"  # Replace with your NewsAPI key
FACT_CHECK_API_KEY = "AIzaSyCaxgI1rS_BiYJZGuOqE5usisbVN_Yh864"  # Replace with Google Fact Check API key

# -----------------------------
# Google Fact Check Function
# -----------------------------
def check_fact_with_google(claim):
    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
    params = {
        "query": claim,
        "key": FACT_CHECK_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        result = response.json()
        if 'claims' in result and len(result['claims']) > 0:
            print("✅ Google Fact Check Result Found:")
            for claim in result['claims'][:1]:
                print(f" - Claim: {claim.get('text')}")
                print(f"   Claimant: {claim.get('claimant')}")
                print(f"   Review: {claim['claimReview'][0].get('textualRating')}")
            return True
        else:
            print("🔴 No fact check result found.")
            return False
    else:
        print("🔴 Error checking Google Fact Check API.")
        return False

# -----------------------------
# NewsAPI Function
# -----------------------------
def fetch_related_news(claim):
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': claim,
        'apiKey': NEWS_API_KEY,
        'pageSize': 5,
        'sortBy': 'relevancy',
        'language': 'en'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        if articles:
            print("🗞 Related News Articles Found:")
            for article in articles[:3]:
                print(f" - {article['title']} ({article['source']['name']})")
                print(f"   URL: {article['url']}\n")
            return True
        else:
            print("❌ No related news articles found.")
            return False
    else:
        print("🔴 Error fetching news articles.")
        return False

# -----------------------------
# Final Verdict
# -----------------------------
def analyze_claim(claim):
    print(f"\n🔍 Analyzing Claim: {claim}\n")
    fact_result = check_fact_with_google(claim)
    news_result = fetch_related_news(claim)

    if fact_result or news_result:
        print("✅ FINAL VERDICT: LIKELY REAL")
        return "REAL"
    else:
        print("⚠️ FINAL VERDICT: INCONCLUSIVE")
        print("📌 Reason: No supporting fact checks or related news found. Cannot verify the claim.")
        return "INCONCLUSIVE"

# -----------------------------
# Example Usage
# -----------------------------
user_claim = "Donald Trump claimed on Saturday that China was hit harder than the United States in the ongoing tariff war triggered by the US president's imposition of reciprocal tariffs on most countries. A day after the US stock markets plummeted, evoking fears of a global recession, the US president claimed his country had been treated unsustainably badly by Beijing and other nations."
analyze_claim(user_claim)

user_claim1 = "Landmine Victims Deserve More Than Sympathy. It's Time for a UN Fund To Support Them"
analyze_claim(user_claim1)