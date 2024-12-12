from pydantic import BaseModel
from typing import Any, Optional


class Result(BaseModel):
    code: int
    message: str
    data: Optional[Any] = None

    @classmethod
    def success(cls, msg: str = "success", data: Any = None):
        return cls(code=1, message=msg, data=data)

    @classmethod
    def fail(cls, msg: str = "error", data: Any = None):
        return cls(code=0, message=msg, data=data)
