from rest_framework.response import Response
from rest_framework import status

class BaseResponse(Response):
    def __init__(self, message=None, success=False, token=None, error=None, user=None, status=status.HTTP_200_OK, user_id=None, **kwargs):
        data = {}
        if success is not None:
            data["success"] = success
        if message is not None:
            data["message"] = message
        if token is not None:
            data["token"] = token
        if error is not None:
            data["error"] = error
        if user is not None:
            data["user"] = user
        if user_id is not None:
            data["user_id"] = user_id
        data.update(kwargs)
        super().__init__(data=data, status=status)