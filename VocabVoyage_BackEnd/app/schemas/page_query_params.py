from pydantic import BaseModel, Field
from typing import Optional


class PageQueryParams(BaseModel):
    page: int = Field(1, description="当前页码，从1开始")
    page_size: int = Field(10, description="每页返回的记录数")
    status: Optional[int] = Field(None, description="解决状态，'已解决' 或 '未解决'") 