# crud/user.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user_word_stats import UserWordStats


async def create_user(db: AsyncSession, nick_name: str, phone: str, password: str):
    new_user = User(nick_name=nick_name, phone=phone, password=password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def get_user_by_phone(db: AsyncSession, phone: str):
    # 使用异步查询
    result = await db.execute(select(User).filter(User.phone == phone))
    return result.scalar_one_or_none()  # 获取查询结果


async def get_user_by_id(db: AsyncSession, user_id: int):
    # 使用异步查询
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalar_one_or_none()  # 获取查询结果


# 验证账号密码, 成功则返回匹配的 user
async def verify_password(db: AsyncSession, phone: str, password: str):
    user = await get_user_by_phone(db, phone)
    if user and user.password == password:
        return user
    return None


async def update_user_password(db: AsyncSession, user_id: int, new_password: str):
    await db.execute(
        update(User)
        .where(User.id == user_id)
        .values(password=new_password)
    )
    await db.commit()


async def update_user_avatar(db: AsyncSession, user_id: int, avatar_url: str):
    await db.execute(
        update(User)
        .where(User.id == user_id)
        .values(avatar=avatar_url)  # 更新头像字段
    )
    await db.commit()


async def update_user_fields(db: AsyncSession, user_id: int, **kwargs):
    # 使用 kwargs 来动态更新用户字段
    await db.execute(
        update(User)
        .where(User.id == user_id)
        .values(**kwargs)  # 将 kwargs 解包为字段和值
    )
    await db.commit()


async def get_user_word_stats_by_id(db: AsyncSession, user_id: int):
    # 查询视图数据
    result = await db.execute(select(UserWordStats).filter(UserWordStats.user_id == user_id))
    stats = result.scalar_one_or_none()  # 获取查询结果

    # 如果没有找到数据，返回零
    if stats is None:
        return {
            "user_id": user_id,
            "total_memorized_words": 0,
            "average_proficiency": 0.0
        }
    
    return stats