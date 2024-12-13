from pydantic import BaseModel, Field
from app.core.constans import Constants


class ProficiencyFilterRequest(BaseModel):
    new_word_weight: float = Field(..., description="生词权重")
    count: int = Field(Constants.DEFAULT_MEMORIZE_WORD_COUNT, description="获取单词数量 (可选)")


class MemorizeWordRequest(BaseModel):
    word_id: int = Field(..., description="单词 id")
    mem_res: int = Field(..., description="记忆结果，1: 认识  2: 模糊  3: 忘记")


class ReportMistakeRequest(BaseModel):
    word_id: int = Field(..., description="单词 id")
    description: str = Field(default="（无描述）", description="错误描述")

