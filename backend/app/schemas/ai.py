from typing import Optional, List, Any
from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str  # "user" | "assistant"
    content: str


class ChatRequest(BaseModel):
    message: str
    history: Optional[List[ChatMessage]] = []


class CaptionRequest(BaseModel):
    topic: str


class AnalyzeRequest(BaseModel):
    username: Optional[str] = None  # для блогера
    artist: Optional[str] = None    # для музыканта


class PitchRequest(BaseModel):
    type: str  # "label" | "playlist"


class AIResponse(BaseModel):
    result: str


class PlanDay(BaseModel):
    day: int
    topic: str
    hook: str
    platform: str
    duration: Optional[str] = None
    publish_time: Optional[str] = None
    format: Optional[str] = None
    idea: Optional[str] = None


class PlanResponse(BaseModel):
    plan: Any
    cached: bool = False
