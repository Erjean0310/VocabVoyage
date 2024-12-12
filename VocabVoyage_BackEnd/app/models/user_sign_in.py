from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserSignIn(Base):
    __tablename__ = "user_sign_in"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="签到记录ID")
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False, comment="用户ID")
    sign_in_year_month = Column(String(16), nullable=False, comment="签到年月")
    record = Column(BIT(32), nullable=False, comment="签到记录")

    __table_args__ = (
        UniqueConstraint("user_id", "sign_in_year_month", name="idx_user_id_year_month"),
    )
