import pandas as pd
import re
from difflib import get_close_matches
from datetime import datetime

courses_df = pd.read_csv("data/courses.csv")
dining_df = pd.read_csv("data/dining.csv")
events_df = pd.read_csv("data/events.csv")
feedback_df = pd.read_csv("data/feedback.csv")
recreation_df = pd.read_csv("data/recreation.csv")
services_df = pd.read_csv("data/services.csv")
study_spaces_df = pd.read_csv("data/study_spaces.csv")

courses_df["full_code"] = courses_df["dept"].str.upper() + courses_df["number"].astype(str)

def clean_input(text):
    replacements = {
        "proffessor": "professor", "lib": "library", "engg": "engineering",
        "caf": "cafeteria", "srvcs": "services", "cntr": "center", "sci": "science"
    }
    text = text.lower().strip()
    for wrong, right in replacements.items():
        text = text.replace(wrong, right)
    return text

def fuzzy_match(query, choices, cutoff=0.6):
    match = get_close_matches(query.lower(), [c.lower() for c in choices], n=1, cutoff=cutoff)
    return next((c for c in choices if c.lower() == match[0]), None) if match else None

def chatbot_response(user_input):
    user_input = clean_input(user_input)
    if "professor" in user_input:
        return "Professor query received."
    elif "study now" in user_input:
        return "Suggesting best study space now."
    return "Sorry, I didn't get that."
