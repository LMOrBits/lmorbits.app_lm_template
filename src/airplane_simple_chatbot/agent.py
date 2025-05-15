from functools import partial
from pyapp.model_connection.model import get_model_lm_from_config_dir
from pyapp.utils.config import find_config
from pathlib import Path
from airplane_simple_retriever.schemas import AnyMessage
from loguru import logger

here = Path(__file__).resolve()
config_dir = find_config(here, "appdeps.toml")
model = get_model_lm_from_config_dir(config_dir=config_dir)


def agent_function(messages: list[AnyMessage]) -> str:
    question = messages[-1].content
    return model.invoke(question)

def get_agent():
    return agent_function
