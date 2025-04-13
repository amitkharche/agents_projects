import os
from dotenv import load_dotenv

def load_openai_key():
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")