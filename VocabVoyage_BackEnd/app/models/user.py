from sqlalchemy import Column, Integer, String
from app.models.base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, comment="用户ID")
    nick_name = Column(String(255), nullable=False, unique=True, comment="用户昵称")
    phone = Column(String(64), unique=True, nullable=True, comment="手机号")
    password = Column(String(255), nullable=False, comment="用户密码")
    coin = Column(Integer, default=0, comment="金币")
    role = Column(String(255), default="user", comment="角色")
