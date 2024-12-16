# service/word.py
import random
from app.core.constans import Constants
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.memory import list_words_by_proficiency, get_proficiency_of_word, update_proficiency
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from app.crud.word import get_word_not_in_list


"""
认识    proficiency  = proficiency * 0.7 + max * 0.3
模糊    proficiency  = proficiency * 0.9
忘记    proficiency  = proficiency * 0.3

         proficiency               划分
生词     0 =< x < 30          p
模糊词   30 <= x < 80      1 - p - fix 
熟词     80 <= x < 101      fix = 0.1
"""


async def handle_memory(db: AsyncSession, user_id, word_id: int, mem_res: int):
    try:
        await db.execute(
            text("CALL update_proficiency(:p_word_id, :p_user_id, :mem_res)"),
            {"p_word_id": word_id, "p_user_id": user_id, "mem_res": mem_res}
        )
        await db.commit()
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

    # proficiency = await get_proficiency_of_word(db, word_id, user_id)
    # match mem_res:
    #     case 1:  # 认识
    #         proficiency = proficiency * 0.7 + 100 * 0.3
    #     case 2:  # 模糊
    #         proficiency = proficiency * 0.9
    #     case 3:  # 忘记
    #         proficiency = proficiency * 0.3
    # proficiency = int(proficiency)
    # await update_proficiency(db, word_id, proficiency, user_id)


async def get_words(db: AsyncSession, user_id: int, new_word_weight, count: int):
    words = []

    familiar_word_weight = Constants.FAMILIAR_WORD_WEIGHT
    familiar_word_count = count * familiar_word_weight
    familiar_word = await list_words_by_proficiency(db, user_id, familiar_word_count, 80, 101)
    words.extend(familiar_word)

    vague_word_count = (count * (1 - new_word_weight - familiar_word_weight)
                        + familiar_word_count - len(familiar_word))
    vague_word = await list_words_by_proficiency(db, user_id, vague_word_count, 30, 80)
    words.extend(vague_word)

    new_word_count = count - len(words)
    new_word = await list_words_by_proficiency(db, user_id, new_word_count, 0, 30)
    words.extend(new_word)

    need = count - len(words)
    # 若单词依然不够
    if need > 0:
        supplementary_word = await get_word_not_in_list(need, words, db)
        words.extend(supplementary_word)

    random.shuffle(words)
    return words