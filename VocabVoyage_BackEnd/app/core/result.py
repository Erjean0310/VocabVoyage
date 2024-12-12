from pydantic import BaseModel
from typing import Any, Optional


class Result(BaseModel):
    status_code: int
    message: str
    data: Optional[Any] = None

    @classmethod
    def success(cls, message: str = "成功", data: Any = None):
        return cls(status_code=200, message=message, data=data)

    @classmethod
    def fail(cls, message: str, status_code: int = 400):
        return cls(status_code=status_code, message=message)
