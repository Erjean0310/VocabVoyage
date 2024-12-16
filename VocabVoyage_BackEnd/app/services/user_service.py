from datetime import datetime
from app.crud.user_sigin_in import add_sign_in_record, get_sign_in_record, update_sign_in_record
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.constans import Constants
from app.common.result import Result


# 用户签到
async def user_sign_in(db: AsyncSession, user_id: int):
    date_string = "2024-01-16"
    cur_date = datetime.strptime(date_string, "%Y-%m-%d")

    # cur_date = datetime.now()  TODO 修复

    day = cur_date.day
    year_month_str = cur_date.strftime("%Y-%m")

    if day == 1:  # 每月 1 号直接添加签到记录
        await add_sign_in_record(db, user_id, 1 << 1, year_month_str)
        return Result.success(Constants.SIGN_IN_SUCCESS)

    record = await get_sign_in_record(db, user_id, year_month_str)

    if record is None:
        record = 1 << day
        await add_sign_in_record(db, user_id, record, year_month_str)
    else:
        offset = 1 << day
        is_signed_in = record & offset
        if is_signed_in:
            return Result.fail(Constants.USER_HAS_SIGNED_IN)
        else:
            record = record | offset
        await update_sign_in_record(db, user_id, record, year_month_str)

    return Result.success(Constants.SIGN_IN_SUCCESS)


# 检查用户登录状态
async def check_sign_in_status(db: AsyncSession, user_id: int):
    cur_date = datetime.now()
    year_month_str = cur_date.strftime("%Y-%m")
    record = await get_sign_in_record(db, user_id, year_month_str)

    if record:
        day = cur_date.day
        offset = 1 << day
        is_signed_in = record & offset
        if is_signed_in:
            return True
    return False


# 获取签到记录
async def handle_sign_in_record(db: AsyncSession, user_id: int, year_month_str: str):
    record = await get_sign_in_record(db, user_id, year_month_str)
    if record is None:
        return []

    # 如果月份是单个数字，去掉前导零
    year, month = year_month_str.split('-')
    if len(month) == 2 and month[0] == '0':
        month = month[1]
    year_month_str = f"{year}-{month}-"

    res = []
    for i in range(1, 8 * int.bit_length(record)):  # 乘以8是因为1字节有8位
        # 检查当前位是否为1
        if (record >> i) & 1:
            res.append(year_month_str + str(i))

    return res






