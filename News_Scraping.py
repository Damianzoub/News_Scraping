import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from googletrans import Translator
import json

URL = 'https://www.protothema.gr/'

results = {
    'positive': [],
    'negative': [],
    'neutral': []
}

translator = Translator()

def categorize_headlines(headline):
    """Categorize a single headline based on its sentiment."""
    polarity = text_analysis(headline)
    if polarity > 0:
        results['positive'].append(headline)
    elif polarity == 0:
        results['neutral'].append(headline)
    else:
        results['negative'].append(headline)

def text_analysis(headline):
    """Translate and analyze sentiment of a headline."""
    try:
        translated = translator.translate(headline, src='el', dest='en').text
        analysis = TextBlob(translated)
        return analysis.sentiment.polarity
    except Exception as e:
        print(f"Error analyzing headline '{headline}': {e}")
        return 0  # Treat as neutral if error occurs

def get_news():
    """Fetch and analyze news headlines."""
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f'Error fetching news: {e}')
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all('div', class_='heading')
    
    headline_set = set()
    for headline in headlines:
        data = headline.get_text(strip=True)
        headline_set.add(data)
    
    print('Analysis of News Headlines:')
    for headline in headline_set:
        categorize_headlines(headline)

    print(f"\nPositive Headlines ({len(results['positive'])}): {results['positive']}")
    print(f"\nNegative Headlines ({len(results['negative'])}): {results['negative']}")
    print(f"\nNeutral Headlines ({len(results['neutral'])}): {results['neutral']}")

    # Save results to JSON
    with open("headline_analysis.json", "w", encoding="utf-8") as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)
    print("\nResults saved to 'headline_analysis.json'.")

if __name__ == "__main__":
    get_news()
