from datetime import datetime
from app.crud.user_sigin_in import add_sign_in_record, get_sign_in_record, update_sign_in_record
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.core.constans import Constants


# 用户签到
async def user_sign_in(db: AsyncSession, user_id: int):
    cur_date = datetime.now()
    day = cur_date.day
    year_month_str = cur_date.strftime("%Y-%m")

    if day == 1:  # 每月 1 号直接添加签到记录
        await add_sign_in_record(db, user_id, 1 << 1, year_month_str)
        return

    record = await get_sign_in_record(db, user_id, year_month_str)

    if record is None:
        record = 1 << day
        await add_sign_in_record(db, user_id, record, year_month_str)
        return
    else:
        offset = 1 << day
        a = type(record)
        is_signed_in = record & offset
        if is_signed_in:
            # 用户已签到
            raise HTTPException(status_code=403, detail=Constants.USER_HAS_SIGNED_IN)
        else:
            record = record | offset
        await update_sign_in_record(db, user_id, record, year_month_str)






