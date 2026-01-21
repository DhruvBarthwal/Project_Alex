from langgraph.graph import StateGraph, END
from agent.state import AgentState

from agent.nodes.read_mails.read_email import read_email_node
from agent.nodes.read_mails.delete_email import delete_email_node
from agent.nodes.read_mails.confirm_delete import confirm_delete_node

from agent.nodes.send_mails.compose_email import compose_email_node
from agent.nodes.send_mails.collect_to import collect_to_node
from agent.nodes.send_mails.collect_subject import collect_subject_node
from agent.nodes.send_mails.collect_body import collect_body_node
from agent.nodes.send_mails.send_email import send_email_node

from utils.llm_intent import classify_intent
from utils.intent_fallback import fallback_intent

def intent_node(state: AgentState):
    if state.get("awaiting_field"):
        print("⏭️ SKIPPING INTENT — awaiting field:", state["awaiting_field"])
        return state

    user_input = state.get("user_input", None)

    intent_from_fallback = fallback_intent(user_input or "")
  
    intent = intent_from_fallback

    if intent == "UNKNOWN":
        try:
            intent = classify_intent(user_input or "")
            
        except Exception as e:
            intent = "UNKNOWN"

    state["intent"] = intent
    return state

def router(state: AgentState):
    awaiting = state.get("awaiting_field")

    if awaiting == "to":
        return "COLLECT_TO"
    if awaiting == "subject":
        return "COLLECT_SUBJECT"
    if awaiting == "body":
        return "COLLECT_BODY"
    if awaiting == "confirm":
        return "SEND_EMAIL" 
    
    return state["intent"]


def build_graph():
    graph = StateGraph(AgentState)
    
    graph.add_node("intent",intent_node)
    graph.add_node("read_email", read_email_node)
    graph.add_node("delete_email", delete_email_node)
    graph.add_node("confirm_delete", confirm_delete_node)
    

    graph.add_node("compose_email", compose_email_node)
    graph.add_node("collect_to", collect_to_node)
    graph.add_node("collect_subject", collect_subject_node)
    graph.add_node("collect_body", collect_body_node)
    graph.add_node("send_email", send_email_node)
    
    graph.set_entry_point("intent")
    
    graph.add_conditional_edges(
        "intent",
        router,
        {
            "READ_EMAIL": "read_email",
            "DELETE_EMAIL": "delete_email",
            "CONFIRM_SEND": "confirm_delete",
            "COMPOSE_EMAIL" : "compose_email",
            
            "COLLECT_TO": "collect_to",
            "COLLECT_SUBJECT": "collect_subject",
            "COLLECT_BODY": "collect_body",
            "SEND_EMAIL": "send_email",
            
            "UNKNOWN": END,
        }
    )
    
    
    return graph.compile()