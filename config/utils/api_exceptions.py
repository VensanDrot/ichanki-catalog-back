from copy import deepcopy

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework.views import exception_handler
from django.utils.translation import gettext_lazy as _

import logging

logger = logging.getLogger()


class APIValidation(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'error'

    def __init__(self, detail=default_detail, code=default_code, status_code=status_code):
        self.status_code = status_code
        super().__init__(detail, code)


def uni_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        if type(response.data) in [ReturnList, list]:
            for key, value in response.data[0].items():
                response.data[0][key] = value[0].strip()
            response.data = {
                'detail': response.data[0],
                'status_code': response.status_code
            }
        else:
            response_data_dict = deepcopy(response.data)
            for key, value in response_data_dict.items():
                if type(value) in [ReturnList, list]:
                    if type(value[0]) is dict:
                        for d_key, d_value in value[0].items():
                            if type(d_value) is list:
                                response.data[d_key] = d_value[0].strip()
                                continue
                            response.data[d_key] = d_value.strip()
                            continue
                        response.data.pop(key)
                        continue
                    response.data[key] = value[0].strip()
                else:
                    response.data[key] = value.strip()
            response.data['status_code'] = response.status_code
    if response:
        if response.status_code == 401:
            response = Response({'detail': _('No active account found with the given credentials'),
                                 'status_code': status.HTTP_401_UNAUTHORIZED}, status=status.HTTP_401_UNAUTHORIZED)
            return response
        return response
