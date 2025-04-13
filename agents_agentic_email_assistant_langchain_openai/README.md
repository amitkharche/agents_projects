# 📧 Agentic AI Email Assistant

This project is an **Agentic AI system** that autonomously classifies and replies to emails using:

- 🤖 Machine Learning for intent classification (Support, Inquiry, etc.)
- 🧠 GPT-powered replies via LangChain and OpenAI
- 🛠️ LangChain Tools and Agent for autonomous reasoning and action

## 🚀 Features
- Upload CSV files with `sender`, `subject`, and `body`
- Classify emails using a trained ML model
- Generate GPT-based replies using LangChain Agent
- Download classified & replied results

## 🛠️ Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key_here
```

Then run:

```bash
streamlit run app/app.py
```

## 📁 Project Structure

```
├── app/
│   └── app.py
├── src/
│   ├── inference.py
│   ├── utils.py
│   └── ...
├── models/
│   └── email_classifier.pkl
├── data/
│   └── raw/
│       └── emails.csv
├── notebooks/
│   └── exploratory_analysis.ipynb
│   └── model_training_and_evaluation.ipynb
├── .env
├── requirements.txt
├── README.md
└── Dockerfile
```

## 🧠 Agentic AI Framing

We use `LangChain Tool` and `initialize_agent()` to enable GPT to act autonomously. This turns a basic assistant into a reasoning agent capable of reacting to new queries and tasks dynamically.