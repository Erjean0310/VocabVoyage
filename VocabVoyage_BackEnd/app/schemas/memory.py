from pydantic import BaseModel, Field
from app.core.constans import Constants


class ProficiencyFilterRequest(BaseModel):
    new_word_weight: float = Field(..., description="生词权重")
    count: int = Field(Constants.DEFAULT_MEMORIZE_WORD_COUNT, description="获取单词数量 (可选)")


