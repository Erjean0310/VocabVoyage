from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy import func, and_
from app.models.memory import Memory


#  根据用户和熟练度范围获取单词ID列表
async def list_words_by_proficiency(db: AsyncSession,  user_id: int, count: int, start: int, end: int):
    result = await db.execute(
        select(Memory.word_id)
        .where(
            and_(
                Memory.user_id == user_id,
                Memory.proficiency >= start,
                Memory.proficiency < end
            )
        )
        .order_by(func.random())
        .limit(count)
    )
    word_ids = result.scalars().all()
    return word_ids


async def get_proficiency_of_word(db: AsyncSession, word_id: int, user_id: int):
    result = await db.execute(
        select(Memory.proficiency).where(
            and_(
                Memory.word_id == word_id,
                Memory.user_id == user_id
            )
        )
    )
    proficiency = result.scalar_one_or_none()
    return proficiency


async def update_proficiency(db: AsyncSession, word_id: int, proficiency: int, user_id: int):
    await db.execute(
        update(Memory).where(
            and_(
                Memory.word_id == word_id,
                Memory.user_id == user_id
            )
        ).values(proficiency=proficiency)
    )
    await db.commit()

