import requests
import json


def chat_with_model(content , prompt , model = "Llama3.1:8b"):
    url = "http://localhost:11434/api/chat"
    data = {
        "model": model,
        "messages": [
            {"role": "system",
             "content": prompt},
            {"role": "user", "content": content}
        ],
        "stream": False
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # 检查请求是否成功
        result = response.json()  # 解析返回的JSON数据
        # print(result["message"]["content"])
        return result


    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP错误: {http_err}")
    except Exception as err:
        print(f"出现错误: {err}")