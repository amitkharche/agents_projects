"""
Summarize text using OpenAI GPT.
"""

import openai

# Replace with env var or secure method
OPENAI_API_KEY = "sk-api_key"
# Note: In a production environment, use environment variables or a secure vault for API keys.

# Function to summarize text using OpenAI's GPT-3.5
import openai

# Create client once
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def summarize_text(text, max_tokens=150):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"Summarize the following text:\n\n{text}"
            }
        ],
        max_tokens=max_tokens
    )
    
    return response.choices[0].message.content
