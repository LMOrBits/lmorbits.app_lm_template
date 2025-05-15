from pyapp.utils.config import get_pyapp_config
from airplane_simple_chatbot.agent import get_agent
from airplane_simple_chatbot.schemas import Config, State

from langgraph.graph import StateGraph
from typing import Optional

from pathlib import Path
config = get_pyapp_config(Config, Path(__file__))
agent = get_agent()



def chatbot(state: State) -> State:
    result = agent(state.messages)
    return {"messages": result}

def add_workflow(graph: StateGraph , end_node: Optional[str] = None, start_node: Optional[str] = None ):
    app_name = "airplane-simple-chatbot"
    chatbot_name = f"{app_name}.chatbot"
    if start_node and end_node:
        graph.add_node(chatbot_name, chatbot)
        graph.add_edge(start_node, chatbot_name)
        graph.add_edge(chatbot_name, end_node)
    elif start_node:
        graph.add_node(chatbot_name, chatbot)
        graph.add_edge(start_node, chatbot_name)
    elif end_node:
        graph.add_node(chatbot_name, chatbot)
        graph.add_edge(chatbot_name, end_node)
        graph.set_entry_point(chatbot_name)
    else:
        graph.add_node(chatbot_name, chatbot)
        graph.set_entry_point(chatbot_name)
    return graph

def get_app():
    graph = StateGraph(State)
    add_workflow(graph)
    return graph.compile()









