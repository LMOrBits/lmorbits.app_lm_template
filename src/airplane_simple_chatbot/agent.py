from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import BaseMessage
from airplane_simple_chatbot.config import model, config
from airplane_simple_retriever.schemas import State as RetrieverState

def agent_function(messages: list[BaseMessage] , documents: list[Document]) -> str:
    prompt = ChatPromptTemplate.from_messages(config.main.to_list()+ messages)
    chain = prompt | model
    if len(documents) > 0:
        return chain.invoke({"documents": documents})
    else:
        return chain.invoke({"documents": "no documents found, we don't have the answer to the question"})

def chatbot(state: RetrieverState) -> RetrieverState:
    result = agent_function(state.messages, state.retriver_results)
    return {"messages": result}