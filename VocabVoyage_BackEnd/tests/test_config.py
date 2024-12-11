import os
from app.core.config import Settings


def test_settings_load_env():
    print(os.path)
    # 检查 .env 文件是否存在
    assert os.path.exists(".env"), ".env file does not exist"

    # 加载 Settings 实例
    settings = Settings()

    # 验证加载的配置是否正确
    assert settings.MYSQL_HOST == "123.249.75.60", f"Expected 123.249.75.60, got {settings.MYSQL_HOST}"
    assert settings.MYSQL_PORT == 3306, f"Expected 3306, got {settings.MYSQL_PORT}"
    assert settings.MYSQL_USER == "root", f"Expected root, got {settings.MYSQL_USER}"
    assert settings.MYSQL_PASSWORD == "768260", f"Expected 768260, got {settings.MYSQL_PASSWORD}"
    assert settings.MYSQL_DB == "vocab_voyage", f"Expected vocab_voyage, got {settings.MYSQL_DB}"

    # 验证生成的 DATABASE_URL
    expected_url = "mysql+aiomysql://root:768260@123.249.75.60:3306/vocab_voyage"
    assert settings.database_url == expected_url, f"Expected {expected_url}, got {settings.database_url}"
    print("test!!!!!!!!!!!!!!!!!!!")


def test_settings_load_env2():
    settings = Settings()
    print(f"Host: {settings.MYSQL_HOST}")
    print(f"Port: {settings.MYSQL_PORT}")
    print(f"User: {settings.MYSQL_USER}")
    print(f"Password: {settings.MYSQL_PASSWORD}")
    print(f"Database: {settings.MYSQL_DB}")
    print(f"Database URL: {settings.database_url}")
    print("luoluoluo")


if __name__ == "__main__":
    test_settings_load_env()
    test_settings_load_env2()

