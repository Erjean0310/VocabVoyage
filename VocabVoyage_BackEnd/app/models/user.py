from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="用户ID")
    nick_name = Column(String(255), comment="昵称")
    phone = Column(String(16), unique=True, nullable=False, comment="手机号")
    password = Column(String(64), comment="用户密码")
    coin = Column(Integer, default=0, comment="金币")
    role = Column(String(255), default="user", comment="角色")
    
    memories = relationship("Memory", back_populates="user")
    sign_in_records = relationship("UserSignIn", back_populates="user")
    reported_mistakes = relationship("Mistake", foreign_keys="Mistake.reporter_id", back_populates="reporter")
    solved_mistakes = relationship("Mistake", foreign_keys="Mistake.solver_id", back_populates="solver")
