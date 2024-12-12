# crud/user.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from sqlalchemy import update


async def create_user(db: AsyncSession, nick_name: str, phone: str, password: str):
    db_user = User(nick_name=nick_name, phone=phone, password=password)
    db.add(db_user)
    await db.commit()  # 异步提交
    await db.refresh(db_user)  # 异步刷新
    return db_user


async def get_user_by_phone(db: AsyncSession, phone: str):
    # 使用异步查询
    result = await db.execute(select(User).filter(User.phone == phone))
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

