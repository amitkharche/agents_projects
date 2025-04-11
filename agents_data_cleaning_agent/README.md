# 🧹 Autonomous Data Cleaning Agent

## 📌 Overview

This assistant automatically detects and fixes:
- Missing values
- Outliers (e.g., extreme ages)
- Date formatting issues
- Standardizes country names and income fields

## 🧠 Powered by
- Pandas for transformations
- LangChain agent logic (expandable with OpenAI)
- Streamlit UI for interaction

## 🚀 How to Use

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

## 📁 Project Structure

```
data_cleaning_agent/
├── data/raw/dirty_customer_data.csv
├── src/data_cleaning_agent.py
├── app/app.py
├── requirements.txt
├── Dockerfile
├── README.md
```
