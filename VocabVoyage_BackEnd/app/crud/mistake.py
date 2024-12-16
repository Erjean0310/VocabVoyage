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
    # 为报告人和解决人创建别名
    user_reporter = aliased(User, name='reporter')
    user_solver = aliased(User, name='solver')
    skip = (page - 1) * page_size
    # 构建查询
    query = (select(
        Mistake,
        Word.spell,
        Word.meaning,
        Word.description,
        user_reporter.nick_name.label("reporter_nick"),
        user_solver.nick_name.label("solver_nick"),
        Mistake.report_time,
        Mistake.resolved_time,
        Mistake.is_resolved
    ).join(Word, Mistake.word_id == Word.id).join(user_reporter, Mistake.reporter_id == user_reporter.id)
             .outerjoin(user_solver, Mistake.solver_id == user_solver.id))

    # 根据状态参数过滤
    if status is not None:
        query = query.where(Mistake.is_resolved == status)

    # 使用分页参数
    query = query.offset(skip).limit(page_size)

    # 计算符合状态的记录总数
    total_query = select(func.count(Mistake.id)).where(Mistake.is_resolved == status if status is not None else True)

    total_result = await db.execute(total_query)
    total = total_result.scalar()

    result = await db.execute(query)
    mistakes = result.all()

    mistake_details = [
        MistakePageQueryVO(
            mistake_id=mistake.id,
            word_spell=spell,
            word_meaning=meaning,
            word_description=description,
            reporter_nick_name=reporter_nick,
            solver_nick_name=solver_nick,
            report_time=report_time,
            resolved_time=resolved_time,
            status="已解决" if is_resolved == 1 else "未解决"
        )
        for mistake, spell, meaning, description, reporter_nick, solver_nick, report_time, resolved_time, is_resolved
        in mistakes
    ]

    return PageQueryResult(mistakes=mistake_details, total=total)
