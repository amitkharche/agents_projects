"""
Summarize text using OpenAI GPT.
"""

import openai

def summarize_text(text, max_tokens=150):
    openai.api_key = "your-api-key-here"  # Replace securely in production
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize the following text:
{text}"}],
        max_tokens=max_tokens
    )
    return response['choices'][0]['message']['content']
