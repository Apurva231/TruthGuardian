import os
from dotenv import load_dotenv
import requests

load_dotenv()

GOOGLE_FACT_CHECK_API_KEY = os.getenv("GOOGLE_FACT_CHECK_API_KEY")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")


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



# -----------------------------
# Configuration
# -----------------------------

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