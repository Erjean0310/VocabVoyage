# service/word.py
import random
from app.core.constans import Constants
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.memory import list_words_by_proficiency


"""
认识    score  = score * 0.7 + max * 0.3
模糊    score  = score * 0.9
忘记    score  = score * 0.3

         score               划分
生词     0 =< x < 30          p
模糊词   30 <= x < 80      1 - p - fix 
熟词     80 <= x < 101      fix = 0.1
"""


async def handle_memory(db: AsyncSession, word_id: int, mem_res: int):
    pass


async def get_words(db: AsyncSession, user_id: int, new_word_weight, count: int):
    words = []

    familiar_word_weight = Constants.FAMILIAR_WORD_WEIGHT
    familiar_word_count = count * familiar_word_weight
    familiar_word = await list_words_by_proficiency(db, user_id, familiar_word_count, 80, 101)
    words.extend(familiar_word)

    a = type(familiar_word)
    print("====", a)

    vague_word_count = (count * (1 - new_word_weight - familiar_word_weight)
                        + familiar_word_count - len(familiar_word))
    vague_word = await list_words_by_proficiency(db, user_id, vague_word_count, 30, 80)
    words.extend(vague_word)

    new_word_count = count - len(words)
    new_word = await list_words_by_proficiency(db, user_id, new_word_count, 0, 30)
    words.extend(new_word)

    random.shuffle(words)
    return words



