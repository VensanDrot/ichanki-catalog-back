from os import remove as delete_file

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.files.models import File
from apps.files.utils import upload_file
from config.utils.api_exceptions import APIValidation


class FileCreateAPIView(APIView):
    def post(self, request):
        if request.FILES:
            file = request.data.get('file')
            if file.size < 20_971_520:
                e_file = upload_file(file=file)
                return Response({
                    "message": "File successfully uploaded",
                    "file": e_file.id,
                    "status": status.HTTP_201_CREATED
                }, status=status.HTTP_201_CREATED)
            else:
                raise APIValidation(detail='Faylning hajmi 20 mb dan oshib ketdi!',
                                    status_code=status.HTTP_400_BAD_REQUEST)
        else:
            raise APIValidation(detail='File was not sent', status_code=status.HTTP_400_BAD_REQUEST)


class FileDeleteAPIView(APIView):

    @staticmethod
    def get_object(pk):
        try:
            return File.objects.get(pk=pk)
        except File.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        file = self.get_object(pk)
        delete_file(file.path)
        file.delete()
        return Response({
            "message": "File successfully deleted",
            "status": status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
