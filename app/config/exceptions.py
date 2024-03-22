from fastapi import status, HTTPException
from pydantic import BaseModel

class APIException(HTTPException):
    """Light wrapper around HTTPException that allows specifying defaults via class property"""

    status_code = status.HTTP_400_BAD_REQUEST
    detail = None
    headers = None

    def __init__(self, *args, **kwargs):
        if "status_code" not in kwargs:
            kwargs["status_code"] = self.status_code
        if "detail" not in kwargs:
            kwargs["detail"] = self.detail
        if "headers" not in kwargs:
            kwargs["headers"] = self.headers
        super().__init__(*args, **kwargs)

"""Custom exception for 404"""

class NotFoundExceptionModel(BaseModel):
    detail: str = "Object not found"

class NotFoundException(APIException):
    status_code = 404
    detail = NotFoundExceptionModel().detail

    def __init__(self, *args, **kwargs):
        if "detail" in kwargs:
            self.detail = kwargs["detail"]
        super().__init__(*args, **kwargs)



