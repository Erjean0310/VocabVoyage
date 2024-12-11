import os
import pandas as pd
from chat import chat_with_model
# from openai_chat import *


prompt = """
# 角色

你是一名中英文双语教育专家，拥有帮助将中文视为母语的用户理解和记忆英语单词的专长，请根据用户提供的英语单词完成下列任务。

## 任务

### 分析词义

- 系统地分析用户提供的英文单词，并以简单易懂的方式解答；

### 列举例句

- 根据所需，为该单词提供至少 3 个不同场景下的使用方法和例句。用词难度逐渐上升，并且附上中文翻译，以帮助用户更深入地理解单词意义。

### 词根分析

- 分析并展示单词的词根；
- 列出由词根衍生出来的其他单词；

### 词缀分析

- 分析并展示单词的词缀，例如：单词 individual，前缀 in- 表示否定，-divid- 是词根，-u- 是中缀，用于连接和辅助发音，-al 是后缀，表示形容词；
- 列出相同词缀的的其他单词；

### 发展历史和文化背景

- 详细介绍单词的造词来源和发展历史，以及在欧美文化中的内涵

### 单词变形

- 列出单词对应的名词、单复数、动词、不同时态、形容词、副词等的变形以及对应的中文翻译。
- 列出单词对应的固定搭配、组词以及对应的中文翻译。

### 单词的派生

- 列出一些由这个单词所衍生出来的词，或者是这个单词其中所包含的核心词汇

### 使用情景

- 提供一些单词的使用情景，以及常见的固定搭配，必要的时候附带上造出的英文语句以及此语句的中文翻译

### 小故事

- 用英文撰写一个有画面感的场景故事，包含用户提供的单词。
- 要求使用简单的词汇，100 个单词以内。
- 英文故事后面附带对应的中文翻译。

"""


# 设置文件路径
words_file = 'data/words.csv'
output_file = 'data/results.csv'

# 检查是否已有结果文件，若存在则读取已处理的单词
if os.path.exists(output_file):
    existing_results = pd.read_csv(output_file)
    processed_words = set(existing_results['word'])
    
    results = existing_results.to_dict(orient="records")
    # print(results)
    # print(type(results))
else:
    processed_words = set()
    results = []



print(processed_words)

# 读取单词列表
words_df = pd.read_csv(words_file)
words = words_df['word'].tolist()




# 处理每个单词
for i, word in enumerate(words):
    if i>100:
        break
    if word in processed_words:
        print(f"单词 '{word}' 已处理，跳过。")
        continue  # 跳过已处理的单词

    try:
        print(f"正在处理单词 {i + 1}/{len(words)}: '{word}'")
        # 调用 chat_with_model 函数获取结果
        result = chat_with_model(word,prompt)
        result = result["message"]["content"]
        results.append({'word': word, 'result': result})

    except Exception as e:
        print(f"处理单词 '{word}' 时出错: {e}")
        results.append({'word': word, 'result': None})  # 记录错误

    # 实时保存到 CSV 文件
    pd.DataFrame(results).to_csv(output_file, index=False)


print("处理完成，结果已保存。")