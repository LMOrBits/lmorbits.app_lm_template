from functools import partial
from pyapp.model_connection.model import get_model_lm_from_config_dir
from pyapp.utils.config import find_config
from pathlib import Path
from airplane_simple_retriever.schemas import AnyMessage
from langchain_core.documents import Document
from loguru import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import BaseMessage
from pyapp.utils.config import get_pyapp_config 
from airplane_simple_chatbot.schemas import Config

here = Path(__file__).resolve()
config_dir = find_config(here, "appdeps.toml")
model = get_model_lm_from_config_dir(config_dir=config_dir)

config = get_pyapp_config(Config, here)



def agent_function(messages: list[BaseMessage] , documents: list[Document]) -> str:
    prompt = ChatPromptTemplate.from_messages(config.main.to_list()+ messages)
    chain = prompt | model
    return chain.invoke({"documents": documents})

