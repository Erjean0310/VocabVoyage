from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# 创建异步数据库引擎
engine = create_async_engine(
    settings.database_url,
    echo=True  # 开发环境下启用 SQL 语句日志
)

# 创建异步会话工厂
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


# 获取数据库会话
async def get_db():
    async with async_session() as session:
        yield session
