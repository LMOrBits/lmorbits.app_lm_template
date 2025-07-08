from langchain_core.messages import HumanMessage

from app_lm_template.graph import get_app
from pyapp.observation.phoneix import traced_agent
import uuid
from pathlib import Path
from app_lm_template.config import app_config
app = get_app()


@traced_agent(name=f"{app_config.project.name}-chatbot")
def app_invoke(messages , session_id: str):
    state = app.invoke({"messages": messages, "session_id": session_id})
    return state["messages"]

def inference():
    messages = [
        HumanMessage(content="When do I need to be at the boarding gate?")
    ]
    session_id = str(uuid.uuid4())
    return app_invoke(messages, session_id)

@traced_agent(name=f"{app_config.project.name}-chatbot")
async def app_stream(messages , session_id: str):
  async for event in app.astream_events(input={"messages": messages, "session_id": session_id}, version="v2",include_names=["Docs","stream"]):
    print(event)
    kind = event["event"]
    if kind == "on_chat_model_stream":
        print(event['data']['chunk'])
    if kind == "on_retriever_end":
      docs = []
      for i,doc in enumerate(event['data']['output']):
        docs.append(doc)


def get_graph():
    from langchain_core.runnables.graph import MermaidDrawMethod
    png_bytes = app.get_graph().draw_mermaid_png(draw_method=MermaidDrawMethod.PYPPETEER)
    with open(Path.cwd() / "airplane_simple_chatbot.png", "wb") as f:
        f.write(png_bytes)
    return app



