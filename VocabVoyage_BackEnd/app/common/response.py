from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse


class CustomException(HTTPException):
    def __init__(self, status_code: int, message: str):
        super().__init__(status_code=status_code, detail=message)


async def general_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"status_code": exc.status_code, "message": exc.detail}
        )
    elif isinstance(exc, CustomException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"status_code": exc.status_code, "message": exc.detail}
        )
    else:
        # 直接构造响应体
        return JSONResponse(
            status_code=500,
            content={"status_code": 500, "message": "内部服务器错误"}
        )