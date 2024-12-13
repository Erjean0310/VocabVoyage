from pydantic import BaseModel, Field
from typing import List, Optional
from app.core.constans import Constants


# 创建一个 Pydantic 模型来接收请求参数
class ChatRequest(BaseModel):
    messages: List[dict] = Field(..., description="聊天消息列表")
    model: Optional[str] = Field(Constants.DEFAULT_MODEL, description="使用模型，默认为 gpt-4o-mini")
    stream: Optional[bool] = Field(Constants.DEFAULT_STREAM_ENABLED, description="是否流式返回，默认为 False")
