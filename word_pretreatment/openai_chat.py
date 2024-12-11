##此py仅用于测试最基础的gpt功能
import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

# client = openai()

# gpt的单次回复
def chat_with_openai(text,prompt, model="gpt-4o-mini"):
    print(text)
    messages = [{"role": "user", "content": prompt},
                {"role": "user", "content": text}]
    
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        # temperature=0,  # 控制模型输出的随机程度
    )
    result = response.choices[0].message.content
    print(result)
    return result




result = chat_with_openai('abash',"你是一个热心的英语老师")
print(result)
# print(result.content)
