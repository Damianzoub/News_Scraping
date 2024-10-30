# Headline Sentiment Analysis

This project fetches Greek news headlines from protothema.gr 

## Features 

- Fetches and translates Greek news headlines because the textblob library supports only English text so we need the googletrans library

- Categorizes headlines based on sentiment polarity (positive, negative, neutral) headlines

- Saves the categorized results in a JSON file for easy review
 

## Installation 

1. Clone the repository:
 ```bash
   git clone https://github.com/Damianzoub/News_Scraping.git

CD News_Scraping

2. Install dependencies:
 ```bash
 pip install -r requirements.txt
 ```

## Usage
Run the analysis script:

``` bash
python News_Scraping.py
