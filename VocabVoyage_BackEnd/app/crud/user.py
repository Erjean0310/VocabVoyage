# crud/user.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User


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


async def verify_password(db: AsyncSession, phone: str, password: str):
    db_user = await get_user_by_phone(db, phone)
    if db_user and db_user.password == password:
        return db_user
    return None
