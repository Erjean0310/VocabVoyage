from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.orm import relationship
from app.models.base import Base


class UserSignIn(Base):
    __tablename__ = "user_sign_in"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="签到记录ID")
    user_id = Column(Integer, ForeignKey("user.id"), comment="用户id")
    sign_in_year_month = Column(String(16), comment="签到年月")
    record = Column(BIT(32), comment="签到记录")

    __table_args__ = (
        UniqueConstraint("user_id", "sign_in_year_month", name="idx_user_id_year_month"),
    )

    user = relationship("User", back_populates="sign_in_records")
