from typing import List, Optional
import openai
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
from app.services.chat import handle_chat  # 导入处理聊天的函数
from app.schemas.chat_resquest import ChatRequest

router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest):  # 使用 ChatRequest 作为请求参数
    messages = request.messages
    model = request.model
    stream = request.stream

    if not messages:
        raise HTTPException(status_code=400, detail="Messages are required")

    response = handle_chat(messages, model, stream)

    if stream:
        return StreamingResponse(response(), media_type='text/event-stream')
    else:
        return response
