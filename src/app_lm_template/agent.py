from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AnyMessage
from app_lm_template.config import model, config
from app_lm_template.schemas import State
from langchain_core.messages.utils import convert_to_openai_messages

def agent_function(messages: list[AnyMessage]):
    # Convert config.main prompts to messages and combine with input messages
    prompt_messages = config.main.to_list() + convert_to_openai_messages(messages)
    prompt = ChatPromptTemplate.from_messages(prompt_messages)
    chain = prompt | model.with_config(run_name="stream")
    return chain

def chatbot(state: State):
    chain = agent_function(state.messages)
    return chain.invoke({})