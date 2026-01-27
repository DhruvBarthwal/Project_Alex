from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from agent.prompts import SYSTEM_PROMPT

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.0,  # IMPORTANT: deterministic extraction
)

MAX_CHARS = 6000


def summarize_email(email_text: str) -> dict:
    """
    Summarizes email content into a structured dictionary.
    Returns factual data only.
    """

    # Very small emails → return as-is (no LLM)
    if not email_text or len(email_text) < 80:
        return {
            "Sender": "Not mentioned",
            "Purpose": "Not mentioned",
            "Key points": [email_text.strip()],
            "Deadlines": "Not mentioned",
        }

    email_text = email_text[:MAX_CHARS]

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=email_text),
    ]

    try:
        response = llm.invoke(messages)
        raw = response.content.strip()
    except Exception as e:
        return {
            "Sender": "Not mentioned",
            "Purpose": "Summarization failed",
            "Key points": ["Unable to summarize this email."],
            "Deadlines": "Not mentioned",
        }

    return _parse_summary(raw)


def _parse_summary(text: str) -> dict:
    """
    Converts LLM text output into a structured dictionary.
    """
    result = {
        "Sender": "Not mentioned",
        "Purpose": "Not mentioned",
        "Key points": [],
        "Deadlines": "Not mentioned",
    }

    current_key = None

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        if line.startswith("Sender:"):
            result["Sender"] = line.replace("Sender:", "").strip()
            current_key = None

        elif line.startswith("Purpose:"):
            result["Purpose"] = line.replace("Purpose:", "").strip()
            current_key = None

        elif line.startswith("Key points:"):
            current_key = "Key points"

        elif line.startswith("Deadlines:"):
            result["Deadlines"] = line.replace("Deadlines:", "").strip()
            current_key = None

        elif line.startswith("Actions required:"):
            result["Actions required"] = line.replace("Actions required:", "").strip()
            current_key = None

        elif current_key == "Key points":
            result["Key points"].append(line.lstrip("- ").strip())

    if not result["Key points"]:
        result["Key points"] = ["Not mentioned"]

    return result
