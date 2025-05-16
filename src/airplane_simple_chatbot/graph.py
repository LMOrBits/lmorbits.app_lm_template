from pyapp.utils.config import get_pyapp_config
from airplane_simple_chatbot.agent import chatbot
from airplane_simple_chatbot.schemas import Config, ChatbotInvoke
from airplane_simple_retriever.schemas import State as RetrieverState
from airplane_simple_retriever.graph import Graph as RetrieverGraph


from langgraph.graph import StateGraph
from typing import Optional

from pathlib import Path
config = get_pyapp_config(Config, Path(__file__))







class ChatbotGraph:
    name = "airplane-simple-chatbot"
    nodes = {
        "single": "chatbot"
    }

    Invoke: ChatbotInvoke


    def get_app(self,graph: StateGraph ):
        chatbot_name = f"{self.name}.chatbot"
        graph = StateGraph(RetrieverState)
        graph.add_node(self.nodes["single"], chatbot) 
        graph.set_entry_point(self.nodes["single"])
        return graph.compile()


class Graph:
    name = "airplane-simple-chatbot"
    nodes = {}
    state = RetrieverState

    def __init__(self):
        chatbot_name = f"{self.name}.answer"
        self.retriever_graph = RetrieverGraph()
        self.nodes = {
            "start": self.retriever_graph.nodes["start"],
            "end": chatbot_name,
            "single": chatbot_name
        }

    def add_workflow(self,graph: StateGraph , end_node: Optional[str] = None, start_node: Optional[str] = None ):
        graph.add_node(self.nodes["single"], chatbot)
        if start_node:
            if end_node:
                self.retriever_graph.add_workflow(graph, end_node=self.nodes["single"], start_node=start_node)
                graph.add_edge(self.nodes["single"], end_node)
            else:
                self.retriever_graph.add_workflow(graph, end_node=self.nodes["single"], start_node=start_node)
        else:
            if end_node:
                self.retriever_graph.add_workflow(graph, end_node=self.nodes["single"])
                graph.add_edge(self.nodes["single"], end_node)
            else:
                self.retriever_graph.add_workflow(graph , end_node=self.nodes["single"])

        return graph



def get_app():
    airplane_simple_retriever_graph = Graph()
    graph = StateGraph(RetrieverState)
    graph = airplane_simple_retriever_graph.add_workflow(graph)
    app = graph.compile()
    return app










