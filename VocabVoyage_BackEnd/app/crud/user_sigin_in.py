from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from app.models.user_sign_in import UserSignIn


async def get_sign_in_record(db: AsyncSession, user_id: int, year_month: str):
    result = await db.execute(
        select(UserSignIn.record)
        .filter(UserSignIn.user_id == user_id, UserSignIn.sign_in_year_month == year_month)
    )
    record = result.scalar_one_or_none()
    a = type(record)
    return record


async def add_sign_in_record(db: AsyncSession, user_id: int, record: int, year_month: str):
    user_sign_in = UserSignIn(user_id=user_id, record=record, sign_in_year_month=year_month)
    db.add(user_sign_in)
    await db.commit()


async def update_sign_in_record(db: AsyncSession, user_id: int, record: UserSignIn, year_month: str):
    await db.execute(
        update(UserSignIn)
        .where(UserSignIn.user_id == user_id, UserSignIn.sign_in_year_month == year_month)
        .values(record=record)
    )
    await db.commit()

