from pyapp.utils.config import get_pyapp_config
from app_lm_template.agent import chatbot
from app_lm_template.schemas import Config, ChatbotInvoke
from app_lm_template.config import app_config
from app_lm_template.schemas import State

from langgraph.graph import StateGraph
from typing import Optional

from pathlib import Path
config = get_pyapp_config(Config, Path(__file__))

class ChatbotGraph:
    name = app_config.project.name
    nodes = {
        "single": "chatbot"
    }

    Invoke: ChatbotInvoke


    def get_app(self,graph: StateGraph ):
        chatbot_name = f"{self.name}.chatbot"
        graph = StateGraph(State)
        graph.add_node(self.nodes["single"], chatbot) 
        graph.set_entry_point(self.nodes["single"])
        return graph.compile()


class Graph:
    name = app_config.project.name
    nodes = {}
    state = State

    def __init__(self):
        chatbot_name = f"{self.name}.chatbot"
        self.nodes = {
            "start": chatbot_name,
            "end": chatbot_name,
            "single": chatbot_name
        }

    def add_workflow(self,graph: StateGraph , end_node: Optional[str] = None, start_node: Optional[str] = None ):
        graph.add_node(self.nodes["single"], chatbot) 

        if start_node and end_node:
            graph.add_edge(start_node, self.nodes["start"])
            graph.add_edge(self.nodes["start"], end_node)
        elif start_node:
            graph.add_edge(start_node, self.nodes["start"])
        elif end_node:
            graph.add_edge(self.nodes["start"], end_node)
            graph.set_entry_point(self.nodes["start"])
        else:
            graph.set_entry_point(self.nodes["start"])
        return graph

def get_app():
    graph = StateGraph(State)
    app_lm_template_graph = Graph()
    graph = app_lm_template_graph.add_workflow(graph)
    app = graph.compile()
    return app
