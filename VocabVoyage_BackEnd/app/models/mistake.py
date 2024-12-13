from sqlalchemy import Column, Integer, ForeignKey, DateTime, SmallInteger, func
from sqlalchemy.orm import relationship
from app.models.base import Base


class Mistake(Base):
    __tablename__ = "mistake"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="id")
    word_id = Column(Integer, ForeignKey("word.id"), comment="单词 id")
    reporter_id = Column(Integer, ForeignKey("user.id"), comment="上报人 id")
    solver_id = Column(Integer, ForeignKey("user.id"), comment="解决人 id")
    report_time = Column(DateTime, server_default=func.now(), comment="上报时间")
    resolved_time = Column(DateTime, default=None, comment="解决时间")
    is_resolved = Column(SmallInteger, default=0, comment="是否解决")

    word = relationship("Word", back_populates="mistakes")
    reporter = relationship("User", foreign_keys=[reporter_id], back_populates="reported_mistakes")
    solver = relationship("User", foreign_keys=[solver_id], back_populates="solved_mistakes")
