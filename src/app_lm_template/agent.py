from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import BaseMessage
from app_lm_template.config import model, config
from app_lm_template.schemas import State

def agent_function(messages: list[BaseMessage] ):
    prompt = ChatPromptTemplate.from_messages(config.main.to_list()+ messages)
    chain = prompt | model.with_config(run_name="stream")  
    return chain

def chatbot(state: State):
    documents = state.retriver_results if len(state.retriver_results) > 0 else "no documents found, we don't have the answer to the question"
    chain = agent_function(state.messages)
    return chain.invoke({"documents": documents})