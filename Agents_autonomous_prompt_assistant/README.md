# 🤖 Autonomous Prompt-Based Assistant

## 📌 Business Case
Companies often have internal documents and FAQs that employees refer to. Automating this with a conversational AI agent improves support efficiency, reduces HR/IT burden, and allows intelligent knowledge access using generative AI.

## 💡 Features
- Built on LangChain + OpenAI + FAISS
- Ingests structured FAQ documents
- Supports interactive Q&A via Streamlit
- Easily extensible to PDFs or enterprise docs

## 🚀 Usage
```bash
pip install -r requirements.txt
python src/agent.py       # To generate vector store
streamlit run app/app.py  # To launch the chatbot UI
```

## 🐳 Docker
```bash
docker build -t company-assistant .
docker run -p 8501:8501 company-assistant
```

## 📂 Structure
- `src/agent.py`: LangChain agent pipeline
- `data/raw/company_faq.csv`: Simulated HR/IT FAQ
- `models/vector_store`: Local FAISS database
- `app/app.py`: Streamlit chatbot interface
