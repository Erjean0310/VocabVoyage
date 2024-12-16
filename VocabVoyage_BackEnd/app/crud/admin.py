from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select
from sqlalchemy.engine import Row
from datetime import datetime


async def table_exists(db: AsyncSession, table_name: str) -> bool:
    # 检查数据库表是否存在
    try:
        result = await db.execute(text(f"""
            SELECT COUNT(*) AS count
            FROM information_schema.tables
            WHERE table_schema = DATABASE() AND table_name = '{table_name}';
        """))
        row: Row = result.fetchone()
        return row.count > 0 if row else False
    except Exception as e:
        return False


async def export_data(db: AsyncSession, table_name: str):
    # 检查表是否存在
    if not await table_exists(db, table_name):
        return False

    # 获取当前日期和时间
    datetime_str = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f"{table_name}_{datetime_str}.csv"  # 文件名
    output_dir = "/var/lib/mysql-files/"  # 输出目录
    # 拼接 SQL 语句
    sql_statement = f"""
    SELECT * INTO OUTFILE '{output_dir}{file_name}'
    FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    FROM {table_name};
    """

    # 执行导出操作
    try:
        await db.execute(text(sql_statement))
        print(f"数据已成功导出到: {output_dir}{file_name}")
        return True
    except Exception as e:
        print(f"导出数据失败: {e}")
        return False

