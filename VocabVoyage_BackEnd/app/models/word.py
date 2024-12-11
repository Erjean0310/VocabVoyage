from sqlalchemy import Column, Integer, String, ForeignKey, Date
from app.models.user import Base


class Word(Base):
    __tablename__ = "word"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="单词ID")
    spell = Column(String(255), nullable=False, comment="单词拼写")
    meaning = Column(String(255), comment="单词含义")
    description = Column(String(1024), comment="单词描述")
