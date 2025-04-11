"""
Email classification module using keyword matching (simulated).
"""
def classify_email(subject, body):
    text = f"{subject} {body}".lower()
    if "meet" in text or "schedule" in text:
        return "meeting"
    elif "report" in text or "performance" in text:
        return "report"
    elif "lunch" in text or "coffee" in text:
        return "personal"
    elif "offer" in text or "deal" in text:
        return "promotion"
    else:
        return "general"
