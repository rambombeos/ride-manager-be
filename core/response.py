from rest_framework.response import Response
from rest_framework import status

class BaseResponse(Response):
    def __init__(self, message=None, error=None, token=None, user=None, status=status.HTTP_200_OK, user_id=None, **kwargs):
        data = {}
        if message is not None:
            data["message"] = message
        if error is not None:
            data["error"] = error
        if token is not None:
            data["token"] = token
        if user is not None:
            data["user"] = user
        if user_id is not None:
            data["user_id"] = user_id
        data.update(kwargs)
        super().__init__(data=data, status=status)