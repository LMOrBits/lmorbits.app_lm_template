from pydantic import BaseModel
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage
from typing import Optional, Literal, List
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langchain_core.messages import AnyMessage
# Define the Prompt data model
class Prompt(BaseModel):
    role: Literal["user", "assistant", "system", "human", "ai", "sys"]
    content: str

    def to_list(self) -> list[dict]:
        return [{"role": self.role, "content": self.content}]
    def to_langchain(self) -> BaseMessage:
        if self.role == "user" or self.role == "human":
            return HumanMessage(content=self.content)
        elif self.role == "assistant" or self.role == "ai":
            return AIMessage(content=self.content)
        elif self.role == "system" or self.role == "sys":
            return SystemMessage(content=self.content)
        else:
            raise ValueError(f"Invalid role: {self.role}")

class Prompts(BaseModel):
    prompts: List[Prompt] = []
    
    def to_prompt_template(self) -> ChatPromptTemplate:
        return ChatPromptTemplate.from_messages([p.model_dump() for p in self.prompts])
    def to_list(self) -> list[dict]:
        return [p.model_dump() for p in self.prompts]
    params: List[str] = []

class Config(BaseModel):
    main: Prompts
    
class State(BaseModel):
    messages: list[AnyMessage]
    session_id: str

class ChatbotInvoke(BaseModel):
    messages: list[BaseMessage]
    documents: list[Document]

