from sqlalchemy import Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserWordStats(Base):
    __tablename__ = 'user_word_stats'  # 视图名称

    user_id = Column(Integer, primary_key=True)
    total_memorized_words = Column(Integer)
    average_proficiency = Column(Float) 