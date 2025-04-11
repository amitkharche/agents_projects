# 📊 Autonomous Market Research Bot

## Overview
This project scrapes and summarizes competitor websites using:
- 🧼 BeautifulSoup + Selenium for web scraping
- 🧠 OpenAI (GPT-3.5) for summarization
- 🎛️ Streamlit interface for interaction

## Example Use Cases
- Competitor landscape summaries
- Industry keyword extraction
- Automated reporting of external intel

## How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run Streamlit App:
```bash
streamlit run app/app.py
```

## Project Structure
```
market_research_bot/
├── data/raw/
├── src/
│   ├── scraper.py
│   └── summarizer.py
├── app/
│   └── app.py
├── notebooks/
│   └── exploratory_analysis.ipynb
├── requirements.txt
├── Dockerfile
└── README.md
```
