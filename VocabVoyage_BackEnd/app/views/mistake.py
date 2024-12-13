from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class MistakePageQueryVO(BaseModel):
    mistake_id: int = Field(..., description="错误记录的唯一标识符")
    word_spell: str = Field(..., description="单词的拼写")
    word_meaning: Optional[str] = Field(None, description="单词的含义")
    word_description: str = Field(..., description="单词的描述")
    reporter_nick_name: str = Field(..., description="上报人的昵称")
    solver_nick_name: Optional[str] = Field(None, description="解决人的昵称（可选）")
    report_time: datetime = Field(..., description="上报时间")
    resolved_time: Optional[datetime] = Field(None, description="解决时间（可选）")
    status: str = Field(..., description="解决状态")

    
    