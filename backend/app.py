from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.schemas import VoiceInput
from agent.graph import build_graph
from utils.gmail_auth import get_gmail_service
from utils.gmail_tools import delete_email

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

graph = build_graph()


@app.get("/")
def hello():
    return {"message": "Backend is running"}


@app.post("/voice")
async def voice_input(payload: VoiceInput):
    
    result = graph.invoke({"user_input": payload.text}) 
    intent = result.get("intent")

    # ---------------- READ EMAIL ----------------
    if intent == "READ_EMAIL":
        email_id= result.get("email_id")
        
        return {
            "response": (
                f"You have a new email.\n"
                f"From {result.get('email_from')}.\n"
                f"Subject: {result.get('email_subject')}.\n"
                f"Message: {result.get('email_body')}"
            ),
            "email_id": email_id,   
        }

    # ---------------- DELETE REQUEST ----------------
    if intent == "DELETE_EMAIL":
        
        if not payload.email_id:
            return {
                "response" : "No email selected to delete."
            }
        return {
            "intent" : "DELETE_EMAIL",
            "email_id" : payload.email_id,
            "response" : "Are you sure you want to delte this email?"
        }

    # ---------------- CONFIRM DELETE ----------------
    if intent == "CONFIRM_SEND":
        
        if not payload.email_id:
            return {
                "response": "There is nothing to confirm."
            }

        service = get_gmail_service()
        delete_email(service, payload.email_id)
        
        return {
            "response": "The email has been deleted successfully.",
            "deleted" : True
        }

    # ---------------- UNKNOWN ----------------
    return {
        "response": "Sorry, I didn't understand that."
    }
