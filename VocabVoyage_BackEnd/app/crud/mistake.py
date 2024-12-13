from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from sqlalchemy.orm import aliased
from app.models.mistake import Mistake
from app.models.word import Word
from app.models.user import User
from app.views.mistake import MistakePageQueryVO
from app.common.page_query import PageQueryResult
from typing import Optional


async def get_mistakes_with_details(db: AsyncSession, page: int = 1, page_size: int = 10, status: Optional[int] = None):
    user_solver = aliased(User)

    # 计算跳过的记录数
    skip = (page - 1) * page_size

    query = select(
        Mistake,
        Word.spell,
        Word.meaning,
        Word.description,
        User.nick_name.label("reporter_nick"),
        user_solver.nick_name.label("solver_nick"),
        Mistake.report_time,
        Mistake.resolved_time,
        Mistake.is_resolved
    ).join(Word, Mistake.word_id == Word.id).join(User, Mistake.reporter_id == User.id).outerjoin(user_solver, Mistake.solver_id == user_solver.id)

    # 根据状态参数过滤
    if status is not None:  # 仅在 status 不为 None 时应用过滤
        query = query.where(Mistake.is_resolved == status)  # 直接使用 status 进行过滤

    # 计算符合状态的记录总数
    total_query = select(func.count()).select_from(Mistake)  # 计算总数
    if status is not None:
        total_query = total_query.where(Mistake.is_resolved == status)  # 根据状态过滤总数

    total_result = await db.execute(total_query)
    total = total_result.scalar()  # 获取总数

    query = query.offset(skip).limit(page_size)  # 使用新的分页参数

    result = await db.execute(query)
    mistakes = result.all()

    mistake_details = [
        MistakePageQueryVO(
            mistake_id=mistake.id,
            word_spell=spell,
            word_meaning=meaning if meaning is not None else None,
            word_description=description,
            reporter_nick_name=reporter_nick,
            solver_nick_name=solver_nick,
            report_time=report_time,
            resolved_time=resolved_time,
            status="已解决" if is_resolved == 1 else "未解决"
        )
        for mistake, spell, meaning, description, reporter_nick, solver_nick, report_time, resolved_time, is_resolved in mistakes
    ]
    
    return PageQueryResult(mistakes=mistake_details, total=total)
