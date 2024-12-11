from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, comment="用户ID")
    nick_name = Column(String(255), nullable=False, unique=True, comment="用户昵称")
    phone = Column(String(64), unique=True, nullable=True, comment="手机号")
    password = Column(String(255), nullable=False, comment="用户密码")
    score = Column(Integer, default=0, comment="积分")
    role = Column(String(255), default="user", comment="角色")
