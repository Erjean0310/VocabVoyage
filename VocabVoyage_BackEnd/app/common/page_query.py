from pydantic import BaseModel, Field
from typing import List, Any


class PageQueryResult(BaseModel):
    total: int = Field(..., description="符合状态的记录总数")
    mistakes: List[Any] = Field(..., description="查询结果列表")