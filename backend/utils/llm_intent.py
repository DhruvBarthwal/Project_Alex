import os
from groq import Groq
from agent.prompts import INTENT_CLASSIFICATION_PROMPT
from utils.intent_fallback import fallback_intent

VALID_INTENTS = {
    "READ_EMAIL",
    "DELETE_EMAIL",
    "COMPOSE_EMAIL",
    "CONFIRM_SEND",
    "UNKNOWN",
}

def classify_intent(user_input: str) -> str:

    fallback = fallback_intent(user_input)
    if fallback != "UNKNOWN":
        return fallback

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not found")

    client = Groq(api_key=api_key)

    prompt = INTENT_CLASSIFICATION_PROMPT.format(
        user_input=user_input
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an intent classifier."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=5,
    )

    intent = response.choices[0].message.content.strip().upper()
    return intent if intent in VALID_INTENTS else "UNKNOWN"
