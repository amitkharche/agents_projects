"""
Auto-reply generator using GPT-3 (simulated).
"""
def generate_reply(label):
    replies = {
        "meeting": "Sure, I’m available. Please send an invite with time and agenda.",
        "report": "Thank you for the update. I’ll review the report and follow up.",
        "personal": "Sounds great! Looking forward to it.",
        "promotion": "Thanks, but I’m not interested right now.",
        "general": "Thanks for reaching out. I’ll get back to you shortly."
    }
    return replies.get(label, replies["general"])
