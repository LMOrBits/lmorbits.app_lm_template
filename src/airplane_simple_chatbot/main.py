from airplane_simple_chatbot.agent import get_agent
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from airplane_simple_chatbot.graph import get_app
from pyapp.observation.phoneix import traced_agent
import uuid
from airplane_simple_chatbot.schemas import AnyMessage

app = get_app()


@traced_agent(name="airplane-simple-chatbot")
def app_invoke(messages: list[dict|AnyMessage], session_id: str):
    state = app.invoke({"messages": messages, "session_id": session_id})
    return state["messages"]

def inference():
    messages = [
        HumanMessage(content="what is the capital of france?")
    ]
    session_id = str(uuid.uuid4())
    return app_invoke(messages, session_id)