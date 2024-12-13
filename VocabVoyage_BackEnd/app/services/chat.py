import openai
from app.core.config import settings
from app.core.constans import Constants


def handle_chat(messages, model, stream):

    # 设置 OpenAI API 密钥
    openai.api_key = settings.OPENAI_API_KEY

    # messages
    prompt = {"role": "system", "content": Constants.OPENAI_PROMPT}
    messages.insert(0, prompt)
    # 调用 OpenAI API 处理聊天逻辑
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        stream=stream
    )
    
    async def event_stream():
        for chunk in response:
            try:
                # 检查 chunk 是否包含预期的结构
                choices = chunk.get('choices', [])
                if choices and 'delta' in choices[0]:
                    content = choices[0].delta.get('content')
                    if content is not None:
                        yield content
            except (IndexError, KeyError):
                continue

    return event_stream if stream else response
