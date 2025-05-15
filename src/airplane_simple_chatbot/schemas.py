from pydantic import BaseModel
from langchain_core.messages import AnyMessage
from langchain_core.messages import AnyMessage
from typing import Optional

class Config(BaseModel):
    prompts: Optional[list[AnyMessage]] = None


class State(BaseModel):
    messages: list[AnyMessage]
    session_id: str