from langgraph.graph import StateGraph, END
from agent.state import AgentState
from utils.llm_intent import classify_intent
from agent.nodes.read_email import read_email_node
from utils.intent_fallback import fallback_intent

def intent_node(state: AgentState):

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
    return state["intent"]


def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("intent",intent_node)
    graph.add_node("read_email", read_email_node)

    graph.set_entry_point("intent")
    
    graph.add_conditional_edges(
        "intent",
        router,
        {
            "READ_EMAIL": "read_email",
            "DELETE_EMAIL": END,
            "CONFIRM_SEND": END,
            "UNKNOWN": END,
        }
    )
    
    return graph.compile()