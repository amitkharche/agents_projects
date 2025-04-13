
# 🤖 Autonomous Prompt-Based Assistant (LangChain + Streamlit)

This project demonstrates an enterprise assistant powered by OpenAI + LangChain using a vector store and agent framework.

## 🔧 Components

- `model_training.py`: Prepares and stores a FAISS vector DB from a company FAQ CSV
- `agent.py`: Loads the vector DB and sets up a RetrievalQA agent
- `app.py`: Streamlit UI to query the assistant

## 🧠 Instructions

1. Update `OPENAI_API_KEY` in both `model_training.py` and `agent.py`.
2. Ensure your data file is located at: `data/raw/company_faq.csv`.
3. Run `model_training.py` to create the vector store.
4. Start the Streamlit app:
   ```bash
   streamlit run app/app.py
   ```

## 🗂 Directory Structure

```
project_root/
│
├── app/
│   └── app.py
│
├── src/
│   ├── model_training.py
│   └── agent.py
│
├── data/raw/
│   └── company_faq.csv  # ← Your FAQ data
│
└── models/vector_store/ # ← Auto-created
```

## ⚠️ Note
This project uses manual API key insertion for demo purposes only.
