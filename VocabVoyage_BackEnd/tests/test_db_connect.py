import pytest
import aiomysql


@pytest.mark.asyncio
async def test_mysql_connection():
    """
    测试 MySQL 数据库连接是否正常
    """
    try:
        # 创建连接池
        pool = await aiomysql.create_pool(
            host="123.249.75.60",
            port=3306,
            user="root",
            password="768260",
            db="vocab_voyage",
            autocommit=True
        )
        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                # 测试执行一条简单的查询
                await cursor.execute("SELECT 1")
                result = await cursor.fetchone()
                assert result == (1,), "MySQL 连接测试失败"
    except Exception as e:
        pytest.fail(f"MySQL 连接失败: {e}")
    finally:
        # 确保连接池被关闭
        pool.close()
        await pool.wait_closed()


if __name__ == '__main__':
    test_mysql_connection()

