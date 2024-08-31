from rest_framework.response import Response
from rest_framework import status

class BaseResponse(Response):
    def __init__(self, message=None, error=None, token=None, user=None, status=status.HTTP_200_OK, user_id=None, **kwargs):
        data = {
            "message": message,
            "error": error,
            "token": token,
            "user": user,
            "user_id": user_id,
        }
        data.update(kwargs)
        super().__init__(data=data, status=status)