# 🧠 AI-Powered Data Cleaning Agent

This project provides an intelligent agent that uses rule-based preprocessing and LangChain + OpenAI for interactive data cleaning, reasoning, and transformation.

## 🔍 Business Use Case

In real-world datasets, inconsistencies in formats, duplicates, and missing values are common. This AI agent:
- Cleans income and country fields
- Standardizes formats
- Leverages GPT for dynamic cleaning feedback

## 📁 Project Structure

- `data/raw/`: Contains dirty dataset
- `src/`: Contains cleaning logic, utils, and feature extraction
- `app/`: Streamlit app for interactive cleaning
- `requirements.txt`: All required packages
- `Dockerfile`: For deployment

## 🚀 How to Run

1. Clone the repo and install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your OpenAI key:
```env
OPENAI_API_KEY=your-api-key
```

3. Start the app:
```bash
streamlit run app/app.py
```

## 🧠 Powered By

- OpenAI GPT-3.5 via LangChain
- Pandas, Streamlit